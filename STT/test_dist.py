from geopy import distance
from geopy.geocoders import Nominatim
import pandas as pd

df=pd.read_csv('journey2.csv')
df.head()

geolocator=Nominatim(user_agent="geoapiExercises")

place1=geolocator.geocode("delhi")
place2=geolocator.geocode("chennai")

print(place1,place2)

lat1,long1=(place1.latitude),(place1.longitude)
lat2,long2=(place2.latitude),(place2.longitude)

loc1=(lat1,long1)
loc2=(lat2,long2)

print(distance.distance(loc1,loc2).km," kms")
