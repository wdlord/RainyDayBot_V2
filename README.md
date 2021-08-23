# RainyDayBot_V2 - has now been updated here : https://github.com/wdlord/RainyDayBot_V3/blob/main/README.md
A new implementation of my bot that texts me if there is a chance of rain tomorrow.

The previous version of this bot ran locally on my computer using the Windows Task Scheduler, which I always saw as a problem. I recently discovered a service called Replit, that acts as an in-browser IDE, with the payed option to have a program always running. I used this opportunity to re-work the bot so that it now works off of the Open Weather Map API, instead of web-scraping from the National Weather Service.

Why did I implement my own requests to the Open Weather Map API reather than using PyOWM? I wanted the improved control and the ease of reading directly from the avaiable Open Weather Map API documentation.
