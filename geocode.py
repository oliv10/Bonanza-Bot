import requests
import json

class LocationData:
    
    def __init__(self, place_id = None, licence = None, osm_type = None, osm_id = None, lat = None, lon = None, display_name = None, address = None, boundingbox = None) -> None:
        self.place_id = place_id
        self.licence = licence
        self.osm_type = osm_type
        self.osm_id = osm_id
        self.lat = lat
        self.lon = lon
        self.display_name = display_name
        self.address = address
        self.boundingbox = boundingbox
        
    def getAddress(self):
        return list(self.address.values())

    def __str__(self) -> str:
        return str([self.place_id, self.licence, self.osm_type, self.osm_id, self.lat, self.lon, self.display_name, self.address, self.boundingbox])

class Geocoode:
    
    def __init__(self, api) -> None:
        self.API = api
        
    def getReverse(self, lon, lat) -> dict:
        url = f"https://us1.locationiq.com/v1/reverse.php?key={str(self.API)}&lat={str(lat)}&lon={str(lon)}&zoom=12&normalizeaddress=1&format=json"
        response = requests.get(url)
        data = json.loads(response.content.decode(response.encoding))
        return data
    
    def getLocationData(self, location: dict):
        return LocationData(place_id = location.get("place_id"), licence = location.get("licence"), osm_type = location.get("osm_type"), osm_id = location.get("osm_id"), lat = location.get("lat"), lon = location.get("lon"), display_name = location.get("display_name"), address = location.get("address"), boundingbox = location.get("boundingbox"))

