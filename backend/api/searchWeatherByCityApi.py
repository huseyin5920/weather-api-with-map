from flask_cors import cross_origin
from service.getWeatherData import GetWeatherData
from flask import request


@cross_origin()
def getWeatherByCity():
    cityName = request.json["cityName"]
    responseWeatherData = GetWeatherData().getWeatherDataByCity(cityName)
    return responseWeatherData
