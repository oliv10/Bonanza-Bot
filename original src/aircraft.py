import time
import threading
from opensky.opensky_api import OpenSkyApi

class AirData():
    
    def __init__(self, icao24: str = None, callsign: str = None, origin_country: str = None, time_position: str = None, last_contact: str = None, longitude: str = None, latitude: str = None, baro_altitude: str = None, on_ground: str = None, velocity: str = None, heading: str = None, vertical_rate: str = None, sensors: str = None, geo_altitude: str = None, squawk: str = None, spi: str = None, position_source: str = None) -> None:
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
        
    def getLastContact(self):
        try:
            return int(self.last_contact)
        except TypeError:
            return None
        
    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude
    
    def getBaroAltitude(self):
        return self.baro_altitude
    
    def getLanded(self):
        return self.on_ground
        
    def getVelocity(self):
        try:
            return int(self.velocity * 1.944) # Adjust to Knots
        except TypeError:
            return None
        
    def getVerticalRate(self):
        try:
            return int(self.vertical_rate * 197) # Adjust to Ft/Min
        except TypeError:
            return None
        
    def __eq__(self, other) -> bool:
        return self.last_contact == other.last_contact
        
    def __str__(self) -> str:
        return str([self.icao24, self.callsign, self.origin_country, self.time_position, self.last_contact, self.longitude, self.latitude, self.baro_altitude, self.on_ground, self.velocity, self.heading, self.vertical_rate, self.sensors, self.geo_altitude, self.squawk, self.spi, self.position_source])

class Aircraft(threading.Thread):
    
    def __init__(self, icao24: str, username: str = None, password: str = None) -> None:
        threading.Thread.__init__(self, daemon=True)
        self.icao24 = icao24
        self.API = OpenSkyApi(username, password)
        self.currentAirData = AirData()
        self.previousAirData = AirData()
        
    def run(self):
        while True:
            self.previousAirData = self.currentAirData
            self.currentAirData = self.getAirData()
            time.sleep(10)
        
    def getAirData(self) -> AirData:
        states = self.API.get_states(icao24=self.icao24)
        try:
            dictionary = states.states[0].__dict__
        except IndexError:
            return AirData()
        return AirData(dictionary.get("icao24"), dictionary.get("callsign"), dictionary.get("origin_country"), dictionary.get("time_position"), dictionary.get("last_contact"), dictionary.get("longitude"), dictionary.get("latitude"), dictionary.get("baro_altitude"), dictionary.get("on_ground"), dictionary.get("velocity"), dictionary.get("heading"), dictionary.get("vertical_rate"), dictionary.get("sensors"), dictionary.get("geo_altitude"), dictionary.get("squawk"), dictionary.get("spi"), dictionary.get("position_source"))
