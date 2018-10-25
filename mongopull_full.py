import csv
from pprint import pprint
import json
import pandas as pd
import pymongo
import ast
import os

 # Create connection variable for Project3 database in MLab
connMLAB = "mongodb://jonathan:Biomed#101@ds137003.mlab.com:37003/project3"


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(connMLAB)

# Connect to a database. Will create one if not already available.
db = client.project3
posts = db.zip_community_test5.find({"response.result":{'$exists':True}})
community = []
for post in posts:
    community.append(post["response"]["result"]["package"]["item"])

community_df = pd.DataFrame(community)
print(community_df.head())

