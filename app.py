from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
app.debug = True

# Load the pre-trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            prediction = model.predict([features])[0]
            prediction_text = f"Wine Quality Score: {prediction}"
        except ValueError:
            prediction_text = "Invalid input. Please enter valid numerical values."
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
