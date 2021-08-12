# albionflipper
https://www.youtube.com/watch?v=hVDjQ-HclJM
THis a video explaining standard use for this spreadsheet


This code takes price data from an API and automatically inputs into the google sheet so you do not have to.
WARNING: Prices are often extremely volatile in Albion and the api is not always up to date, especially for lower volume items.
Please always check prices before buying, use this tool and the sheets as a guideline on what to check first for good deals
and what can be quickly skipped.

Credit to the creator of the sheet Big Lips McGee on YT
https://www.youtube.com/channel/UCMiiehUAHfg7KrfaPAk4R0w
Here is a link to his YT

And to the Albion online data project that has collected all the price data we use
https://www.albion-online-data.com/ here is a link to their website


REQS:
https://developers.google.com/sheets/api/quickstart/python
Follow this guide to install the google sheets API
A gservice account and a project (Code will not go over api limits for free usage if used properly)
https://docs.wso2.com/display/IntegrationCloud/Get+Credentials+for+Google+Spreadsheet
Use instructions here to properly set one up

https://developers.google.com/workspace/guides/create-credentials
Follow this guide to properly create a json file of the credentials you will need, after you download add to this folder

https://docs.google.com/spreadsheets/d/13W8j3kCdMdxZiTNHierlkaoAuoQULQT3Me2rhJS9Np4/edit?usp=sharing
Make a copy of this spreadsheet and share it with your service account created earlier, give it editing privileges.
Feel free to change its name but make sure to copy it exactly into the code later.

Copy name of json file and the name of the google sheets you copied into data.py

You are now ready to use this code! Run main.py and all the data from albion online data will be added
