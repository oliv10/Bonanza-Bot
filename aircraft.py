import time
import threading
from opensky.opensky_api import OpenSkyApi

class AirData():
    
    def __init__(self, icao24: str, callsign: str, origin_country: str, time_position: str, last_contact: str, longitude: str, latitude: str, baro_altitude: str, on_ground: str, velocity: str, heading: str, vertical_rate: str, sensors: str, geo_altitude: str, squawk: str, spi: str, position_source: str) -> None:
        self.icao24 = icao24
        self.callsign = callsign
        self.origin_country = origin_country
        self.time_position = time_position
        self.last_contact = last_contact
        self.longitude = longitude
        self.latitude = latitude
        self.baro_altitude = baro_altitude
        self.on_ground = on_ground
        self.velocity = velocity
        self.heading = heading
        self.vertical_rate = vertical_rate
        self.sensors = sensors
        self.geo_altitude = geo_altitude
        self.squawk = squawk
        self.spi = spi
        self.position_source = position_source
        
    def __str__(self) -> str:
        return str([self.icao24, self.callsign, self.origin_country, self.time_position, self.last_contact, self.longitude, self.latitude, self.baro_altitude, self.on_ground, self.velocity, self.heading, self.vertical_rate, self.sensors, self.geo_altitude, self.squawk, self.spi, self.position_source])

class Aircraft(threading.Thread):
    
    def __init__(self, icao24: str, username: str = None, password: str = None) -> None:
        threading.Thread.__init__(self, daemon=True)
        self.icao24 = icao24
        self.API = OpenSkyApi(username, password)
        self.currentAirData = None
        
    def run(self):
        while True:
            self.currentAirData = self.getAirData()
            time.sleep(10)
        
    def getAirData(self) -> AirData:
        states = self.API.get_states(icao24=self.icao24)
        dictionary = states.states[0].__dict__
        return AirData(dictionary.get("icao24"), dictionary.get("callsign"), dictionary.get("origin_country"), dictionary.get("time_position"), dictionary.get("last_contact"), dictionary.get("longitude"), dictionary.get("latitude"), dictionary.get("baro_altitude"), dictionary.get("on_ground"), dictionary.get("velocity"), dictionary.get("heading"), dictionary.get("vertical_rate"), dictionary.get("sensors"), dictionary.get("geo_altitude"), dictionary.get("squawk"), dictionary.get("spi"), dictionary.get("position_source"))
