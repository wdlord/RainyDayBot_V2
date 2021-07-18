import os
from pyowm.owm import OWM


# an object containing forecast information for tomorrow.
class Tomorrow:

  # class constructor
  def __init__(self, location=(33.1192, -117.0864)):
    self.precipitation_probability = None
    self.detailed_status = None
    self.rain = None
    self.location = location

    self.get_data()

  # gets the rain data we want from Open Weather Map
  def get_data(self):
    api_key = os.environ['API_KEY']

    owm = OWM(api_key)
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=self.location[0], lon=self.location[1])
    tomorrow = one_call.forecast_daily[0]

    self.detailed_status = tomorrow.detailed_status
    self.rain = tomorrow.rain
    self.precipitation_probability = tomorrow.precipitation_probability

  # function that builds the message string
  def forecast_string(self): 
    forecast = f'Expect {self.detailed_status}. '
    forecast += f'Probability of Precipitation is {self.precipitation_probability * 100}%. '
    if self.rain:
      forecast += f'Projected rainfall is {self.rain["all"]} mm.'

    return forecast
