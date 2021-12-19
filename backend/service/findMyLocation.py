import geocoder
from constants import constants
from flask import jsonify


class FindMyLocation():
    def __init__(self):
        self.fromApi = constants.FIND_LOCATION_FROM_IP
        self.locateInfo = {}

    def getMyLocation(self):
        g = geocoder.ip(self.fromApi)
        self.locateInfo["latitude"] = g.latlng[0]
        self.locateInfo["longitude"] = g.latlng[1]
        self.locateInfo["city"] = g.city
        return self.locateInfo
