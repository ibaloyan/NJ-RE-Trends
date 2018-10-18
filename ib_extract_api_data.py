# API request to ATTOMdata

# ATTOMDATA call
import http.client

import ib_proj3_config

conn = http.client.HTTPSConnection("search.onboard-apis.com")


headers = {

   'accept': "application/json",

   'apikey': API_KEY,

   }


## conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=4529%20Winona%20Court&address2=Denver%2C%20CO", headers=headers)
# Manalapan county
conn.request("GET", "/communityapi/v2.0.0/Area/Full/?AreaId=CO34025", headers=headers)

# Getting all NJ Zip codes
# https://search.onboard-apis.com/areaapi/v2.0.0/geoid/lookup/?geoId=ST34&GeoType=ZI


# https://search.onboard-apis.com/communityapi/v2.0.0/Area/Full/?AreaId=CO44003

# Getting all NJ geo_keys and latitude and longtitude and county names
# https://search.onboard-apis.com/areaapi/v2.0.0/county/lookup?StateId=ST34

# Getting full commmunity data by state 
# https://search.onboard-apis.com/communityapi/v2.0.0/area/full?AreaId=ZI07726

##   <item type="ST" id="ST34" name="New Jersey" abbreviation="NJ" geo_key="ST34" geo_center_latitude="40.1072740000" geo_center_longitude="-74.6652010000" />

# Response Body
# <?xml version="1.0" encoding="utf-8" ?>
# <response xmlns="https://search.onboard-apis.com/xmlns/areaapi/v2.0.0">
#   <status code="0" short_description="Success" long_description="Your request was successfully processed." />
#   <inputparameter service="Area" resource="county" package="lookup" StateId="ST34"/>
#   <result xml_record="21" >
#     <package name="Lookup" resource="County" service="Area" version="2.0" descr="This lookup returns all the Counties that are in a particular state. The State ID is required. The two-digit FIPS code or the two-letter abbreviation can be used for the State ID." notice="">
#       <item type="CO" id="CO34001" name="Atlantic" geo_key="CO34001" geo_center_latitude="39.4693540000" geo_center_longitude="-74.6337580000" />
#       <item type="CO" id="CO34003" name="Bergen" geo_key="CO34003" geo_center_latitude="40.9596990000" geo_center_longitude="-74.0747270000" />
#       <item type="CO" id="CO34005" name="Burlington" geo_key="CO34005" geo_center_latitude="39.8757860000" geo_center_longitude="-74.6630060000" />
#       <item type="CO" id="CO34007" name="Camden" geo_key="CO34007" geo_center_latitude="39.8023520000" geo_center_longitude="-74.9612510000" />
#       <item type="CO" id="CO34009" name="Cape May" geo_key="CO34009" geo_center_latitude="39.0861430000" geo_center_longitude="-74.8477160000" />
#       <item type="CO" id="CO34011" name="Cumberland" geo_key="CO34011" geo_center_latitude="39.3284340000" geo_center_longitude="-75.1216280000" />
#       <item type="CO" id="CO34013" name="Essex" geo_key="CO34013" geo_center_latitude="40.7874000000" geo_center_longitude="-74.2462920000" />
#       <item type="CO" id="CO34015" name="Gloucester" geo_key="CO34015" geo_center_latitude="39.7228750000" geo_center_longitude="-75.1456790000" />
#       <item type="CO" id="CO34017" name="Hudson" geo_key="CO34017" geo_center_latitude="40.7313750000" geo_center_longitude="-74.0786010000" />
#       <item type="CO" id="CO34019" name="Hunterdon" geo_key="CO34019" geo_center_latitude="40.5652830000" geo_center_longitude="-74.9119690000" />
#       <item type="CO" id="CO34021" name="Mercer" geo_key="CO34021" geo_center_latitude="40.2825030000" geo_center_longitude="-74.7037240000" />
#       <item type="CO" id="CO34023" name="Middlesex" geo_key="CO34023" geo_center_latitude="40.4396130000" geo_center_longitude="-74.4075790000" />
#       <item type="CO" id="CO34025" name="Monmouth" geo_key="CO34025" geo_center_latitude="40.2870480000" geo_center_longitude="-74.1524460000" />
#       <item type="CO" id="CO34027" name="Morris" geo_key="CO34027" geo_center_latitude="40.8585810000" geo_center_longitude="-74.5474270000" />
#       <item type="CO" id="CO34029" name="Ocean" geo_key="CO34029" geo_center_latitude="39.8656690000" geo_center_longitude="-74.2588640000" />
#       <item type="CO" id="CO34031" name="Passaic" geo_key="CO34031" geo_center_latitude="41.0378900000" geo_center_longitude="-74.2982800000" />
#       <item type="CO" id="CO34033" name="Salem" geo_key="CO34033" geo_center_latitude="39.5738280000" geo_center_longitude="-75.3573560000" />
#       <item type="CO" id="CO34035" name="Somerset" geo_key="CO34035" geo_center_latitude="40.5655270000" geo_center_longitude="-74.6199380000" />
#       <item type="CO" id="CO34037" name="Sussex" geo_key="CO34037" geo_center_latitude="41.1374610000" geo_center_longitude="-74.6919140000" />
#       <item type="CO" id="CO34039" name="Union" geo_key="CO34039" geo_center_latitude="40.6598710000" geo_center_longitude="-74.3086960000" />
#       <item type="CO" id="CO34041" name="Warren" geo_key="CO34041" geo_center_latitude="40.8534910000" geo_center_longitude="-75.0094980000" />
#     </package>
#   </result>
# </response>


res = conn.getresponse()

data = res.read()



print(data.decode("utf-8"))