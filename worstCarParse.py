# Parses the "MyWorstCar" hashtag to tabulate general population experience
# of worst car brand
from config import *
import json
import tweepy
import plotly.io as pio
from operator import itemgetter

# Use twitter API to get collection of #MyWorstCar posts
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'MyWorstCar'
print("How many Tweets would you like to parse through?")
num = int(input())
try:
	search_results = tweepy.Cursor(api.search, q = query, lang = 'en').items(num)
except:
	print("Please enter an appropriate number of tweets")
	print("An error code 429 means you have used all of your available API calls")

# Search each post for brand (Toyota, pontiac, bmw, etc.)
brands = {"Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti",
"Buick", "Cadillac", "Caterham", "Chevrolet", "Chrysler", "Dodge", "Ferrari", "Fiat",
"Ford", "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar", "Jeep", "Kia", "Lamborghini",
"Land", "Rover","Lexus", "Lincoln", "Lotus", "Maserati", "Mazda", "Mercedes", "Benz",
"Mini", "Mitsubishi", "Nissan", "Porsche", "Ram", "Rolls Royce", "Smart", "Subaru", "Toyota",
"Tesla", "Volkswagen", "Volvo"}

brandsCount = {"Acura": 0, "Alfa Romeo": 0, "Aston Martin": 0, "Audi": 0, "Bentley": 0, "BMW": 0, "Bugatti": 0,
"Buick": 0, "Cadillac": 0, "Caterham": 0, "Chevrolet": 0, "Chrysler": 0, "Dodge": 0, "Ferrari": 0, "Fiat": 0,
"Ford": 0, "GMC": 0, "Honda": 0, "Hyundai": 0, "Infiniti": 0, "Jaguar": 0, "Jeep": 0, "Kia": 0, "Lamborghini": 0,
"Land": 0, "Rover": 0,"Lexus": 0, "Lincoln": 0, "Lotus": 0, "Maserati": 0, "Mazda": 0, "Mercedes": 0, "Benz": 0,
"Mini": 0, "Mitsubishi": 0, "Nissan": 0, "Porsche": 0, "Ram": 0, "Rolls Royce": 0, "Smart": 0, "Subaru": 0, "Toyota": 0,
"Tesla": 0, "Volkswagen": 0, "Volvo": 0, "Unknown": 0}


for tweet in search_results:
    ttext = tweet.text
    match = next((x for x in brands if x in ttext), False)
    if match == False:
    	brandsCount["Unknown"] += 1
    else:
    	brandsCount[match] += 1

# Print results using plotly
brandsList = brandsCount.items()
sorted(brandsList, key=itemgetter(1))

brandsListx = []
brandsListy = []

for item in brandsList:
	if item[0] == "Unknown":
		print("Number of tweets with no manufacturer found: " + str(item[1]))
	else:	
		brandsListx.append(item[0])
		brandsListy.append(item[1])


fig = dict({
	"data": [{"type": "bar",
	"x": brandsListx,
	"y": brandsListy }],
	"layout": {"title": {"text": "#MyWorstCar Trends"}}
	})

pio.show(fig)