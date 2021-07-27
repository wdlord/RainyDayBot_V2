from Tomorrow import OWM
import Send_SMS
import schedule, time


def rainy_day_bot():

  # check Tomorrow.py for optional OWM() arguments
  tomorrow = OWM()

  if tomorrow.will_rain():
    forecast = tomorrow.forecast_string()
    Send_SMS.send_message("FORECAST ", forecast)

  # prints forecast and other useful info to console
  tomorrow.debug_log()


# MAIN program
# --------------------------
print("the bot has started...")

# for testing
run_now = input("would you like to run the bot now? (y/n)")
if run_now == 'y':
  rainy_day_bot()

# NOTE: this server runs on GMT Timezone, adjust schedules accordingly
schedule.every().day.at("02:00").do(rainy_day_bot)

# infinite loop
while True:
  schedule.run_pending()
  time.sleep(1)
