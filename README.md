# AWS-Concert-Email-List
AWS Lambda function that scrapes songkick.com for bands that are playing in the NY area. Creates a custom message and sends it to my email address via SNS

## Notes about setup
In BandScraper.py the following environment variables are configured:

- BucketName; name of the bucket that has the Bands.json file
- BandJSON; file key for the Bands.JSON file
- SNSARN; the ARN of the SNS topic that sends the email to the appropriate person

Location is currently hard coded to Brooklyn and New York (NYC). These are the songkick location tags and if users want info on shows outside of these two cities, they'd need to update that code.

Bands.JSON will need to be configured for each individual user (unless you only want my band notifications). There may be an easier way, but i just went to each artist's page on songkick.com and got the IDs that way. Good enough for only 30 or so artists.

Users will need to configure an SNS topic to include their desired email address, then use the resulting ARN for the environment variable listed above. This is very easy to do and the free tier of SNS is 1000 emails/year.

The deployment package is ready to go as is, environment variables can be configured in the AWS Lambda Console, just remember the names you configure have to match the names in the script

Currently the Lambda is set to be triggered by a weekly CloudWatch event. This can be updated to whatever interval the user prefers in the Lambda dashboard

## TO DO
Some stuff i got lazy about (set to list to sort, for example) and there are probably more elegant ways to parse the HTML. I also should add more logging too.
