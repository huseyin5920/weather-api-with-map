from flask_cors import cross_origin
from service.findMyLocation import FindMyLocation


@cross_origin()
def getCurrentLocation():
    responseGeoLocation = FindMyLocation().getMyLocation()
    return responseGeoLocation
