import folium
import phonenumbers
from phonenumbers import geocoder
from myphone import number

pepnumber = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number, "RO")
s=carrier.name_for_number(service_pro, "en")
print(s)

from opencage.geocoder import OpenCageGeocode

key = '6d6f969fd9024ac8afde957f0c86a5ba'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

file2write = open("data", 'a')
file2write.write("location "+str(location)+"\n"+"latitude "+str(lat)+" longitude "+str(lng)+"\n"+"Service Provider "+str(s)+"\n\n")
file2write.close()

myMap.save("Templates/mylocation.html")

# import phonenumbers
# from phonenumbers import geocoder
# #from test import number
# import folium
#
# Key = "6d6f969fd9024ac8afde957f0c86a5ba"
#
# number = input("Enter phone number with country code:")
# check_number = phonenumbers.parse(number)
# number_location = geocoder.description_for_number(check_number, "en")
# print(number_location)
#
#
# from phonenumbers import carrier
# service_provider = phonenumbers.parse(number)
# print(carrier.name_for_number(service_provider, "en"))
#
# from opencage.geocoder import OpenCageGeocode
# geocoder = OpenCageGeocode(Key)
#
# query = str(number_location)
# results = geocoder.geocode(query)
#
# lat = results[0]['geometry']['lat']
# lng = results[0]['geometry']['lng']
# print(lat,lng)
#
# map_location = folium.Map(location = [lat,lng], zoom_start=9)
# folium.Marker([lat,lng], popup=number_location).add_to(map_location)
# map_location.save("Templates/mylocation.html")
#
