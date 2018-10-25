import csv
from pprint import pprint
import json
import pandas as pd
import pymongo
import ast
import os

 # Create connection variable for Project3 database in MLab
#     mongodb://<dbuser>:<dbpassword>@ds137003.mlab.com:37003/project3
#         connMLAB = 'mongodb://localhost:27017'
# connMLAB = "mongodb://ibaloyan:francis99@ds137003.mlab.com:37003/project3"
connMLAB = "mongodb://jonathan:Biomed#101@ds137003.mlab.com:37003/project3"

# connMLAB = "mongodb://grothjd:Biomed#101@ds137003.mlab.com:37003/"


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(connMLAB)

# Connect to a database. Will create one if not already available.
# db = client.Apple_y_y
# Fix done for Heroku deployment
# db = client.heroku_8nx1c4b9
db = client.project3
posts = db.zip_community_test5.find({"response.result":{'$exists':True}})
zips = []
for post in posts:
    zips.append(post["response"]["result"]["package"]["item"][0]["geo_code"])
with open("zips.csv","w") as file:
    zipwriter = csv.writer(file)
    zipwriter.writerow(zips)
