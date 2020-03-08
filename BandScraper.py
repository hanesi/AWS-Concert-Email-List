import requests
import json
from bs4 import BeautifulSoup
import datetime

msgList = set()
def parser(idDict):
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
                        msgList.add(msg)
                        print(msg)
            except:
                pass

parser(bandDict)
