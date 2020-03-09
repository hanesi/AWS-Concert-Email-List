# AWS-Concert-Email-List
AWS Lambda function that scrapes songkick.com for bands that are playing in the NY area. Creates a custom message and sends it to my email address via SNS

## Notes about setup
In BandScraper.py the following environment variables are configured:

- BucketName; name of the bucket that has the Bands.json file
- BandJSON; file key for the Bands.JSON file
- SNSARN; the ARN of the SNS topic that sends the email to the appropriate person

Bands.JSON will need to be configured for each individual user (unless you only want my band notifications). There may be an easier way, but i just went to each artist's page on songkick.com and got the IDs that way. Good enough for only 30 or so artists.

The deployment package is ready to go as is, environment variables can be configured in the AWS Lambda Console, just remember the names you configure have to match the names in the script

## TO DO
Some stuff i got lazy about (set to list to sort, for example) and there are probably more elegant ways to parse the HTML. I also should add more logging too.
