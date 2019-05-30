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
from cluster.Cluster import RealestateClustering
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

    # if values are not populated, it means that they are not important for the user
    parks = request.form['parks']
    if parks == "":
        parks = 10
    price = request.form['price']
    if price == "":
        price = 0
    tax = request.form['tax']
    if tax == "":
        tax = 10
    schools = request.form['schools']
    if schools == "":
        schools = 10
    crime = request.form['crime']
    if crime == "":
        crime = 10
    transportation = request.form['transportation']
    if transportation == "":
        transportation = 10
    eats = request.form['eats']
    if eats == "":
        eats = 10
    income = request.form['income']
    if income == "":
        income = 0
    shop = request.form['shop']
    if shop == "":
        shop = 10


    ## Convert money to digits only for price and income
    # price = '$1,425,232' -> price ='1425232'

    price = price.replace("$","").replace(",","")
    income = income.replace("$","").replace(",","")

    input_dict = {'parks': int(parks), 'eats': int(eats), 'shop': int(shop), 'income': int(income), 'price': int(price), 'transportation': int(transportation), 'tax': int(tax)}

    zips_dict = RealestateClustering(input_dict)
    #input_predict = [input_list]
    #predicted = model.predict(input_predict)

    #zip_cluster_vals = pd.DataFrame([ins, labels],).transpose().values
    #zip_cluster = pd.DataFrame(zip_cluster_vals, columns=['zip_code', 'label'])
    #zips_predicted = zip_cluster.loc[zip_cluster['label'] == predicted[0]]
    #zips = zips_predicted['zip_code'].values
    #zips_dict = {'zips': []}
    #for zip in zips:
    #    zips_dict['zips'].append("0" + str(zip))

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

