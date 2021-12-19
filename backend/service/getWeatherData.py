# python_test.py
import requests
from constants import constants


class GetWeatherData():
    def __init__(self):
        self.url = constants.BASE_URL
        self.apiKey = constants.API_KEY

    def getWeatherDataByCity(self, city_name):
        responseWeatherData = requests.get(
            self.url + "appid=" + self.apiKey + "&q=" + city_name + "&lang=tr" + "&units=metric")
        weatherDataByCity = responseWeatherData.json()
        return weatherDataByCity
