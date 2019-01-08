import json,urllib
from urllib.request import urlopen
s=input("Enter the Source:")
d=input("Enter the Destination:")

json_url=urlopen("https://maps.googleapis.com/maps/api/directions/json?origin="+s+"&destination="+d+"")

data=json.loads(json_url.read()) #reading all data


routesdata=data["routes"]
routesfirstdict=routesdata[0]
legsdict=routesfirstdict['legs']
legsfirstdict=legsdict[0]
distdict=legsfirstdict["distance"]

print("Total distance:",distdict["text"])
