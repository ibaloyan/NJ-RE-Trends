# import dependencies
from flask import Flask, render_template, jsonify, request, redirect
from flask_pymongo import PyMongo
import pickle
max_vals = pickle.load( open( "max_vals.p", "rb" ) )
model = pickle.load( open( "model.p", "rb" ) )
ins = pickle.load( open( "ins.p", "rb" ) )
labels = model.labels_
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import the function to return the ML'd data here

# init the Flask
app = Flask(__name__)

#
@app.route("/NJRE")
def njre():
    # create a link to whatever the zipcodes data source will be under here
    # Will most likely be AWS link
    # app.config["MONGO_URI"] = 'mongodb://localhost:27017/NJRE_test'
    # mongo = PyMongo(app)
    # db = mongo.db

    # # create a variable containing the data
    # prefZips = db.flask_test.find_one()

    # #testing json
    # # prefZips = {
    # #     "zipcodes": ['07001', '07002', '07003'],
    # #     "Rating": [.62, .3, .08],
    # #     "Lat": [-72, -60, -65],
    # #     "Long": [120, 118, 110]
    # # }
    # print(prefZips)
    # prefZips_zip = prefZips["zipcodes"]
    # prefZips_rat = prefZips["rating"]
    # prefZips_lat = prefZips["Lat"]
    # prefZips_long = prefZips["Long"]
    
    # # convert the pulled data into a json to render
    # prefZips_dict  = {"zipcode":prefZips_zip, 'rating':prefZips_rat, 'Lat': prefZips_lat, 'Long': prefZips_long}
    return render_template('results.html')
    # return jsonify("returning something back")


# create a index route
@app.route('/')
def index():
    # Return the template 
    return render_template('index.html')

@app.route('/output_page', methods=['POST'])
def Out():
    
    parks = request.form['parks']
    price = request.form['price']
    tax = request.form['tax']
    schools = request.form['schools']
    crime = request.form['crime']
    transportation = request.form['transportation']
    eats = request.form['eats']
    income = request.form['income']
    shop = request.form['shop']

    
    
    parks = (int(parks)/10)*max_vals['recreation']
    tax = (int(tax)/10)*max_vals['avg_prop_tax']
    transportation = (int(transportation)/10)*max_vals['trwpublic']
    eats = (int(eats)/10)*max_vals['eating-drinking']
    shop = (int(shop)/10)*max_vals['shopping']
    input_list = [int(parks), int(eats), int(shop), int(income), int(price), int(transportation), int(tax)]
    input_predict = [input_list]
    predicted = model.predict(input_predict)

    zip_cluster_vals = pd.DataFrame([ins, labels],).transpose().values
    zip_cluster = pd.DataFrame(zip_cluster_vals, columns=['zip_code', 'label'])
    zips_predicted = zip_cluster.loc[zip_cluster['label'] == predicted[0]]
    zips = zips_predicted['zip_code'].values
    zips_dict = {'zips': []}
    for zip in zips:
        zips_dict['zips'].append("0" + str(zip))

    
    # return render_template('results.html')
    return jsonify(zips_dict)
    # return render_template('results.html', **zips_dict)
    # """
    # parks: %s
    # price: %s
    # tax: %s 
    # schools: %s
    # crime: %s
    # transportation: %s
    # eats: %s
    # income: %s
    # shop: %s
    # """ % (parks, price, tax, schools, crime, transportation, eats, income, shop)
    # put on pre line% (eats)


if __name__ == "__main__":
    app.run(debug=True)

