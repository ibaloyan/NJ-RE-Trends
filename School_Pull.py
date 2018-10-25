
# coding: utf-8

# In[1]:


import http.client
# from ib_proj3_config import API_KEY
from jons_config import api_key
from pprint import pprint
import json
import pandas as pd
import time
import pymongo
import ast
import os


# In[2]:


zips = pd.read_csv("zips.csv")
zip_list = list(zips)


# In[25]:


zip_latlong = pd.read_csv("data/zip_codes_states.csv")
zip_latlong.set_index("zip_code", inplace=True)
int_zip = []
for zipp in zip_list:
    try:
        int_zip.append(int(zipp))
    except:
        int_zip.append(int(round(float(zipp))))
nj_zips = zip_latlong.loc[int_zip]


# In[21]:


lats = list(nj_zips['latitude'])
long = list(nj_zips['longitude'])


# In[ ]:


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


# In[ ]:


# loop through all zip codes
for n in range(len(zip_list)):

    conn = http.client.HTTPSConnection("search.onboard-apis.com")

    headers = {

       'accept': "application/json",
       'apikey': api_key,

       }
## conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=4529%20Winona%20Court&address2=Denver%2C%20CO", headers=headers)
# Manalapan county
# conn.request("GET", "/communityapi/v2.0.0/Area/Full/?AreaId=CO34025", headers=headers)
# conn.request("GET", "/communityapi/v2.0.0/Area/Full/?AreaId=ZI07726", headers=headers)
        
#     com_url = '/propertyapi/v1.0.0/property/expandedprofile?address1=' + firstPart + "&address2=" + secondPart + "%2C+NJ"
#     conn.request("GET", com_url, headers=headers) 
    conn.request("GET", "/propertyapi/v1.0.0/school/snapshot?latitude=" + str(lats[n]) + "&longitude=" + str(long[n]) +  "&radius=5&filetypetext=public", headers=headers)

    # Get response record in json format
    res = conn.getresponse()
    
    



    data = res.read()
    ###print(data)
    # print(res)

#     import json
#     pprint(json.loads(json.dumps(zip_com_json)))
#     #print(json.dumps(json.loads(zip_com_json)))   

        
    # pprint(data.decode("utf-8")
    null = None 
    zip_com_json = eval(data.decode("utf-8"))
    #pprint(zip_com_json["school"])   
    
    try:
        # Creates a collection in the database and insert document
        for item in zip_com_json["school"]:
            db.schools.insert_one(
                item
            )
    except:
        pass

