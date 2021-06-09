# AirNowProject

## What does this project do?
This project retrieves real-time (by the hour) air quality data (particulate matter PM2.5) from a chosen zip code from the AirNow API, parses that JSON and creates a workable python object from it, passes it through some logic which attaches the appropriate color from the [U.S. Air Quality Index (AQI)](https://www.airnow.gov/aqi/aqi-basics/) to the retreived values, and then passes that info to my home's Hue Lights bridge, where it can change a lamp with a hue light to the appropriate color that reflects the current air quality. I used Windows Task Scheduler to make this code run on the hour. Further TODO is to get this synced up with AWS rather than just my own machine running task scheduler. 

## Why am I doing this?
I am personally invested in issues of air quality because I have asthma and the air quality is heavily tied to my quality of life. This helps me make better data-driven decisions by a quick easy glance at my lamp; for example, 'Is is a good time to open the window?' 'Is a good time for me to go on a walk?' etc. 

I started this project so I could practice with real-time data, Python, and APIs, but ultimately all of this is a very practical attempt at improving my own life personally with data applications.

## What is AirNow?
From their [documentation](https://docs.airnowapi.org/docs/MonitoringSiteFactSheet.pdf): "The U.S. Environmental Protection Agency’s (EPA) nationwide, voluntary program, AirNow (www.airnow.gov), provides real-time air quality data and forecasts to protect public health across the United States, Canada, and parts of Mexico. AirNow receives real-time ozone and PM2.5 data from over 2,500 monitors and collects air quality forecasts for more than 500 cities."

## Why am I working with AirNow data?
I am working with AirNow data because after surveying different air quality data sources, this seemed to be a fairly credible (government run, not private) source which provides the data pretty easily with an API.

## AirNow's Data Use Disclaimer
"All data provided by AirNow API are made possible by the efforts of more than 150 local, state, tribal, provincial, and federal government agencies (www.airnow.gov/index.cfm?action=airnow.partnerslist). These data are not fully verified or validated; they should be considered preliminary and are subject to change. Data and information reported to AirNow from federal, state, local, and tribal agencies are for the express purpose of reporting and forecasting the Air Quality Index (AQI).Therefore, they should not be used to formulate or support regulation, trends, guidance, or any other government or public decision making. Official regulatory air quality data must be obtained from EPA’s Air Quality System (AQS) (https://www.epa.gov/aqs). See the AirNow Data Exchange Guidelines at http://airnowapi.org/docs/DataUseGuidelines.pdf." 

## Useful Links
- AirNow [homepage](https://www.airnow.gov/)
- AirNow API [documentation](https://docs.airnowapi.org/)
- AirNow API [FAQs](https://docs.airnowapi.org/faq)
- AirNow API [Data Use Guidlines](https://docs.airnowapi.org/docs/DataUseGuidelines.pdf)
- [Getting started developing with Hue](https://developers.meethue.com/develop/get-started-2/)