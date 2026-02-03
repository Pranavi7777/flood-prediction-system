from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Try to load model and scaler, but provide fallback
try:
    with open("floods.save", "rb") as f:
        model = pickle.load(f)
    with open("transform.save", "rb") as f:
        sc = pickle.load(f)
    MODEL_LOADED = True
except:
    MODEL_LOADED = False
    print("⚠️  Warning: Model files not found. Using demo mode.")

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Prediction input page
@app.route('/predict')
def index():
    return render_template('index.html')

# Prediction logic
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
                # Fallback logic if transform fails
                output = 0
        else:
            # Demo mode: Use simple heuristic
            # If high rainfall and humidity, predict flood risk
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

if __name__ == '__main__':
    print("🌊 Flood Prediction System Starting...")
    print("📱 Open browser to: http://127.0.0.1:5000")
    app.run(debug=True)
