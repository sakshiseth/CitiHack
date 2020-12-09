import requests, json

class getWeatherForecastDetails():
    api_key = "f444f5d92d7cd78bab6cd1a7a47123f5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = 'Delhi'
    def getDetails(self,city):
        self.city_name = city
        complete_url = ''
        complete_url = complete_url + self.base_url + "appid=" + self.api_key + "&q=" + self.city_name
        response = requests.get(complete_url)
        return response.json()["weather"][0]["description"]

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
'''
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
    '''