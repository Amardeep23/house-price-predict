from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

util.load_saved_artifacts()

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_area_names', methods=['GET'])
def get_area_names():
    response = jsonify({
        'area_names': util.get_area_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']
    area_type = request.form['area_type']

    response = jsonify({
        'estimated_home_price': util.get_estimated_price(location, total_sqft, bhk, bath, area_type)
    })
    return response

if __name__ == "__main__":
    print("Staring Python Flask Server For Home Price Prediction....")
    app.run()
