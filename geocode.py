import requests
import json

def reverse(lon: str, lat: str) -> dict:
    # url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en"
    url = f"https://us1.locationiq.com/v1/reverse.php?key=pk.a30d2870922069481cd242be4cdaa9d5&lat={lat}&lon={lon}&addressdetails=0&namedetails=1&normalizeaddress=1&format=json"
    response = requests.get(url)
    data = json.loads(response.content.decode(response.encoding))
    return data