# RainyDayBot_V2
A new implementation of my bot that texts me if there is a chance of rain tomorrow.

The previous version of this bot ran locally on my computer using the Windows Task Scheduler, which I always saw as a problem. I recently discovered a service called Replit, that acts as an in-browser IDE, with the payed option to have a program always running. I used this opportunity to re-work the bot so that it now works off of the Open Weather Map API, instead of web-scraping from the National Weather Service.

If you want to implement this bot here are the steps you can take:
1. Get a Premium Replit account, at the time of writing this the price is $50 annually.
2. Create a new Replit project and copy all the files I included here into the Replit.
3. Add the following Secret variables to your replit: 
  a) API_KEY - this is your Open Weather Map API key, you can make a free account with them
  b) EMAIL - your email address used for sending SMS messages (requires you to enable the account to use 3rd party apps)
  c) PASSWORD - this is your app password for the email address
  d) PHONE - the phone number you want the bot to text
4. in main.py, rain_day_bot() definition add your coordinate location to the Tomorrow() constructor as shown in the comment in the file.
5. In main.py, set the time you want to receive the text in GMT time-zone.
6. 6. Set the Replit project to be "always on".
