from pymongo import MongoClient
import pymongo
# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.House_adds
# Store the entire team collection in a list
info = list(db.house_locs.find())
# marstest = info[0]
print(info[0])
# print(info)

import json

with open('house_ad.json', 'w') as fp:
    json.dumps(info[0], fp)
    
# import csv
 
# # # dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# w = csv.writer(open("house_ad_to_mlab.csv", "w"))
# for key, val in info[0].items():
#     w.writerow([key, val])