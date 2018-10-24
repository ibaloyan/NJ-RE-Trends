# import dependencies
from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
# import the function to return the ML'd data here

# init the Flask
app = Flask(__name__)

#
@app.route("/NJRE")
def njre():
    # create a link to whatever the zipcodes data source will be under here
    # Will most likely be AWS link
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/NJRE_test'
    mongo = PyMongo(app)
    db = mongo.db

    # create a variable containing the data
    prefZips = db.flask_test.find_one()

    #testing json
    # prefZips = {
    #     "zipcodes": ['07001', '07002', '07003'],
    #     "Rating": [.62, .3, .08],
    #     "Lat": [-72, -60, -65],
    #     "Long": [120, 118, 110]
    # }
    print(prefZips)
    prefZips_zip = prefZips["zipcodes"]
    prefZips_rat = prefZips["rating"]
    prefZips_lat = prefZips["Lat"]
    prefZips_long = prefZips["Long"]
    
    # convert the pulled data into a json to render
    prefZips_dict  = {"zipcode":prefZips_zip, 'rating':prefZips_rat, 'Lat': prefZips_lat, 'Long': prefZips_long}
    return jsonify(prefZips_dict)
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

    
    
    # return render_template('results.html')
    return """
    parks: %s
    price: %s
    tax: %s 
    schools: %s
    crime: %s
    transportation: %s
    eats: %s
    income: %s
    shop: %s
    """ % (parks, price, tax, schools, crime, transportation, eats, income, shop)
    # put on pre line% (eats)


if __name__ == "__main__":
    app.run(debug=True)

