#Script to write file of seatgeek ticket prices over time for any of below listed event IDs
import requests, json
#Sturgill/Childers at MSG May 16 - 5088679
#WS Game 4 - 4959419
#UVA vs Duke NCAA Hoops JPJ Feb 28 - 4998086
#UVA UNC Hoops JPJ Dec 7 - 5115025
geekdata = requests.get('https://api.seatgeek.com/2/events/4998086?client_id=NTcxNzY4M3wxNTcxOTU2NzczLjgx&client_secret=1343f67d5c217b44590f663e72c345a6a4a1ae7e9cedbc6663ad951c8305ea48')
geekjson = geekdata.json()
geekresp = json.dumps(geekjson)

import datetime
import pytz
est = pytz.timezone("US/Eastern")
timestamp = str(datetime.datetime.now(est))[5:19]
print ("Last Run at: ", timestamp)

listings = geekjson['stats']['listing_count']
visiblelistings = geekjson['stats']['visible_listing_count']
med = geekjson['stats']['median_price']
avg = geekjson['stats']['average_price']
lowestgooddeal = geekjson['stats']['lowest_price_good_deals']
lowest = geekjson['stats']['lowest_price']
lowestbase = geekjson['stats']['lowest_sg_base_price']
lowestgoodbase = geekjson['stats']['lowest_sg_base_price_good_deals']

text = ["Listings", "visiblelistings", "med", "avg", "lowestgooddeal", "lowest", "lowestbase", "lowestgoodbase", "timestamp"]
textstr = str(text)

print (geekjson['title'])
print ("Listings = ", listings, ", Visible Listings = " , visiblelistings)
print ("Median = " , med)
print ("Average = " , avg)
print ("Lowest good deal = " , lowestgooddeal)
print ("lowest = " , lowest)
print ("Lowest good deal base = " , lowestgoodbase)
print ("lowest base = " , lowestbase)

data = [str(listings), str(visiblelistings), str(med), str(avg), str(lowestgooddeal), str(lowest), str(lowestbase), str(lowestgoodbase), timestamp]


import csv
with open('seatgeekdata.csv', "a") as csv_file:
         writer = csv.writer(csv_file, delimiter=',')
         writer.writerow(data)
