from flask import Flask
from constants import constants
from api import (
    searchWeatherByCityApi,
    findCurrentLocationApi
)

app = Flask("app")


app.add_url_rule(
    "/weatherByCity", view_func=searchWeatherByCityApi.getWeatherByCity, methods=["POST"]
)

app.add_url_rule(
    "/findMyLocation", view_func=findCurrentLocationApi.getCurrentLocation, methods=["GET"]
)
if __name__ == "__main__":
    app.run(constants.FLASK_HOST, constants.FLASK_PORT, debug=True)
