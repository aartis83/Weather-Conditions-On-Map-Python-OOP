from folium import Map

#Get latitude and longtitude values
latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int("-1"))

#Add 180 for negative longitudes
#Subtract 180 for positive longitudes
if longitude.__le__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")
elif longitude.__gt__(float("180")):
    antipode_longitude = str("Invalid Longitude")
else:
    antipode_longitude = longitude.__sub__(float("180"))

location = list((antipode_latitude, antipode_longitude))
mymap = Map(location)
mymap.save(str("antipode.html"))

print(antipode_latitude)
print(antipode_longitude)
print(mymap)