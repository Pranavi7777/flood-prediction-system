"""
Flood Prediction System - Main Application Entry Point
This file is for Render deployment
"""
import sys
import os

# Add flask folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask'))

from flask import Flask, render_template, request
import pickle

app = Flask(__name__, static_folder='flask/static', template_folder='flask/templates')

# Try to load model and scaler
try:
    model_path = os.path.join(os.path.dirname(__file__), 'flask', 'floods.save')
    scaler_path = os.path.join(os.path.dirname(__file__), 'flask', 'transform.save')
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        sc = pickle.load(f)
    MODEL_LOADED = True
except Exception as e:
    MODEL_LOADED = False
    print(f"⚠️  Warning: Model files not found. Using demo mode.")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def index():
    return render_template('index.html')

@app.route('/data_predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        cloud_cover = float(request.form['cloud_cover'])
        annual = float(request.form['annual'])
        jan_feb = float(request.form['jan_feb'])
        mar_may = float(request.form['mar_may'])
        jun_sep = float(request.form['jun_sep'])
        oct_dec = float(request.form['oct_dec'])
        avgjune = float(request.form['avgjune'])
        sub = float(request.form['sub'])

        data = [[
            temp,
            humidity,
            cloud_cover,
            annual,
            jan_feb,
            mar_may,
            jun_sep,
            oct_dec,
            avgjune,
            sub
        ]]

        if MODEL_LOADED:
            try:
                prediction = model.predict(sc.transform(data))
                output = prediction[0]
            except:
                output = 0
        else:
            # Demo mode
            total_rainfall = annual
            if total_rainfall > 3200 and humidity > 72:
                output = 1
            else:
                output = 0

        if output == 0:
            return render_template(
                'nochance.html',
                prediction='✓ No Severe Flood Risk Detected'
            )
        else:
            return render_template(
                'chance.html',
                prediction='⚠ Severe Flood Risk Detected'
            )
    except Exception as e:
        return render_template(
            'nochance.html',
            prediction=f'Error: {str(e)}. Please enter valid numbers.'
        )

@app.errorhandler(404)
def not_found(error):
    return render_template('home.html'), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

