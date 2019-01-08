from geopy.geocoders import Nominatim
geolocator = Nominatim()
l=input("Enter place:")
location = geolocator.geocode(""+l+"")
print(location.address)
print((location.latitude, location.longitude))

