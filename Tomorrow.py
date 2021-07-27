import requests
from datetime import datetime
import os


# function used to get tomorrow's daily forecast object from Open Weather Map
def get_tomorrow(lat, lon, units='imperial', part='minutely'):
  base_url = 'http://api.openweathermap.org/data/2.5/'
  API_key = os.environ['API_KEY']
  response = requests.get(base_url + f'onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}')
  daily_forecast = response.json()['daily']

  return daily_forecast[1]


# used to communicate with Main
class OWM:
  
  # NOTE: coordinates can be verified using this link (change values in address):
  # https://www.latlong.net/c/?lat=33&long=-117

  def __init__(self, location=(33.1192, -117.0864)):
    self.tomorrow = get_tomorrow(location[0], location[1])

  def will_rain(self):
    return self.tomorrow['weather'][0]['main'] == 'Rain'

  def forecast_string(self):
    weather = self.tomorrow['weather'][0]
    forecast = f"Expect {weather['description']}. Probability of precipitation is {self.tomorrow['pop'] * 100}%. "

    return forecast

  def debug_log(self):
    print("\n DEBUG LOG:")
    print(f"Printing info for {datetime.fromtimestamp(self.tomorrow['dt'])}")
    print(self.tomorrow['weather'][0]['main'])
    print(self.forecast_string())
