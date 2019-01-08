import json,urllib
from urllib.request import urlopen
from geopy.geocoders import Nominatim


geolocator = Nominatim(timeout=11)
loc=input("Enter the location: ")
location = geolocator.geocode(""+loc+"")
print(location.address)

print((location.latitude, location.longitude))

lat=str(location.latitude)
long=str(location.longitude)





json_url=urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat+","+long+"&radius=3000&type=restaurant&keyword=cruise&key=AIzaSyDtdOLHYwj63-F3aELjSXDBc-7P7AIKABs")

data=json.loads(json_url.read())


places=data["results"]

'''
a=places[0]
b=places[1]
c=places[2]


print(a['name'],b['name'],c['name'])
'''

c=len(places)

l=[]
for i in range(0,c):
    l.append(places[i])
#print(len(l))

d=len(l)
print()
for i in range(0,d):
    a=l[i]
    print(a['name'])







    
