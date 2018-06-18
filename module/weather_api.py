import os
import sys
import json
import requests

class OpenWeatherAPI(object):
    """
    Performs requests to the OpenWeather API Service.
        Documentation : https://openweathermap.org/api
    # NOTE: - Add more features to this API
            - Publish to PyPi
    """

    def __init__(self, key, headers=None, debug_mode=False, *args,**kwargs):
        self.key = key
        self.debug = debug_mode
        self.args = args
        self.kwargs = kwargs

        self.baseurl = 'https://api.openweathermap.org/data/2.5/'

        if (headers != None):
            self.headers = headers
        else :
            self.headers = {
                "User-agent": "curl/7.43.0",
                "Content-type": "application/json",
                "User-key": self.key
            }

    def current_weather(self, **option):
        """ Get current weather data by city name """

        option['appid'] = self.key

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']

        weather_url = self.baseurl + 'weather'
        response = requests.get(url=weather_url, params=option, headers=self.headers)
        if (self.debug):
            print(response.url)

        return response.json()
