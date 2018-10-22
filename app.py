# import dependencies
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
# import the function to return the ML'd data here

# init the Flask
app = Flask(__name__)

#
@app.route("/NJRE")
def njre():
    # create a link to whatever the zipcodes data source will be under here
    # Will most likely be AWS link
    # app.config["MONGO_URI"] = 'mongodb://localhost:27017/NJre'
    # mongo = PyMongo(app)
    # db = mongo.db

    # create a variable containing the data
    # prefZips = db.NJre.find_one()

    #testing json
    prefZips = {
        "zipcodes": ['07001', '07002', '07003'],
        "Rating": [.62, .3, .08],
        "Lat": [-72, -60, -65],
        "Long": [120, 118, 110]
    }
    # print(prefZips)
    # prefZips_1 = prefZips["<>"]
    
    # convert the pulled data into a json to render
    # prefZips_dict  = {key:value}
    return jsonify(prefZips)


# create a index route
@app.route('/')
def index():
    # Return the template 
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

