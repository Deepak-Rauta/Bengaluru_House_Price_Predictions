# from flask import Flask, request, jsonify
# import util
# app = Flask(__name__)
#
# @app.route('/get_location_names')
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])
#
#     response = jsonify({
#         'locations': util.get_estimated_price(total_sqft, location, bhk, bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# if __name__=='__main__':
#     print("Flask server was ready to run!")
#     app.run()


from flask import Flask, request, jsonify
import util
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)  # Enable Cross-Origin requests for testing

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']  # Corrected to string
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Flask server is ready to run!")
    util.load_saved_artifacts()  # Load artifacts before running the app
    app.run()
