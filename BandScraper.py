import requests
import json
from bs4 import BeautifulSoup
import datetime
import boto3
import os

s3 = boto3.client('s3', 'us-east-1')
sns_client = boto3.client("sns")
obj = s3.get_object(Bucket=os.environ["BucketName"], Key=os.environ["BandJSON"])
fileContents = obj['Body'].read().decode('utf-8')
json_content = json.loads(fileContents)


def lambda_handler(event, context):
    concertList = list(parser(json_content))
    concertList.sort()
    s = "\n".join(i for i in concertList)
    response = sns_client.publish(
        TopicArn=os.environ["SNSARN"],
        Subject="Weekly Concert Update!",
        MessageS=f"The following concerts are upcoming:\n{s}"
    )

def parser(idDict):
    msgSet = set()
    for k, v in idDict.items():
        url = f"https://www.songkick.com/artists/{v}-{k}/calendar"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text,"html")
        data = soup.findAll('script')

        allTourDates = soup.findAll('script', type="application/ld+json")
        for i in allTourDates:
            try:
                test = json.loads(i.text)
                address_info = test[0]['location']['address']
                if address_info['addressLocality'] == 'Brooklyn' or address_info['addressLocality'] == 'New York (NYC)':
                    date = datetime.datetime.strptime(test[0]['endDate'], "%Y-%m-%d")
                    today = datetime.datetime.now()
                    date_diff = (date - today).days
                    if  date_diff < 0:
                        break
                    else:
                        venue = test[0]['location']['name']
                        date = test[0]['endDate']
                        band = test[0]['name']
                        msg = f"{band} is playing at {venue} on {date}"
                        msgSet.add(msg)
            except:
                pass
    return msgSet
