from tomorrow_owm import Tomorrow
import send_sms
import schedule, time

def rainy_day_bot():

  # to run elsewhere, pass location as tuple, careful with NESW signs
  # for example: tomorrow = Tomorrow(location=(33.4255, -111.9400)) is (N, W)
  tomorrow = Tomorrow()

  if tomorrow.precipitation_probability > 0.2:
    forecast = tomorrow.forecast_string()
    print(forecast)
    send_sms.send_message("FORECAST ", forecast)


# MAIN program
print("the bot has started...")

# NOTE: this server runs on GMT Timezone, adjust scedules accordingly
schedule.every().day.at("02:00").do(rainy_day_bot)

# infinite loop
while True:
  schedule.run_pending()
  time.sleep(1)