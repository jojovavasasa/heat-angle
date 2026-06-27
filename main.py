import geocoder
import weatherkit
from time import gmtime, strftime
import tkinter

print(strftime("%H:%M:%S", gmtime()))
g = geocoder.ip("me")
lat, lon = g.latlng
lat = float(lat)
lon = float(lon)
print("using:", lat, "&", lon)
location = weatherkit.current_weather(lat, lon)
rizz = location.temperature()
print(rizz)
