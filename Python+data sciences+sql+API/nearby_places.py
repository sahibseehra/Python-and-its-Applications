from geopy.geocoders import Nominatim
import json,urllib
from urllib.request import urlopen
geolocator = Nominatim()
l=input("Enter place:")
location = geolocator.geocode(""+l+"")
print(location.address)
print((location.latitude, location.longitude))
a=str(location.latitude)
b=str(location.longitude)



json_url=urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+a+","+b+"&radius=5000&type=restaurant&keyword=cruise&key=AIzaSyBDbfy5Rpn-vRIExs9-7d7IrCx9ShKePUA")
data=json.loads(json_url.read())
places=data["results"]
c=len(places)

l=[]
for i in range(0,c):
    l.append(places[i])
#print(len(l))

d=len(l)
print()
b=[]
for i in range(0,d):
    a=l[i]
    #print(a['name'])
    b.append(a['name'])

print(b)

'''obj1=resultsdata[0]
r1=obj1['name']

obj2=resultsdata[1]
r2=obj2['name']

obj3=resultsdata[2]
r3=obj3['name']

obj4=resultsdata[3]
r4=obj4['name']
print(r1)
print(r2)
print(r3)
print(r4)'''
