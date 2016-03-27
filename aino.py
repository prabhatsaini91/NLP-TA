import re, pprint, nltk, pywapi, string, time

##Code for weather and location analysis goes here

##live_loc = live_location()
##loc_id = pywapi.get_location_ids('live_loc')
##locs.append(key for key in loc_id.iterkeys())
##location = locs[1]

location_id = "INXX0096"
location_name = "New Delhi"
weather_com_result = pywapi.get_weather_from_weather_com(location_id)
date = time.strftime("%A %B %d %Y")
t = time.strftime("%I %M %p")

speak = "Hi. Today's " + time.strftime("%A %d") + " of " + time.strftime("%B %Y") + ". The time is " + time.strftime("%I %M %p") + ". It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + " degree celsius now in " + location_name + ". My name is AINO. How do you do? What is your name?"
print speak

intro = raw_input("$ ")

print intro

##def live_location() :
	##this function would be in future hope to gather live geocoded locations via google's api
	##use code here when this is possible
##print tagged_words
