from flask import Flask, render_template, request, jsonify
import numpy
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model
scalar = pickle.load(open('scaling.pkl', 'rb'))
reg = pickle.load(open('regmodel.pkl',  'rb'))

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.form.to_dict()

        # Convert data to a Pandas DataFrame (adjust based on your data)
        #input_data = pd.DataFrame.from_dict(data, orient='index').transpose()
        input_data = list(data.values())
        # Perform any necessary data preprocessing

        # Make a prediction using the loaded model
        x = numpy.array(input_data)
        x=x.reshape(1,-1)
        x =scalar.transform(x)
        prediction = reg.predict(x)

        # Return the prediction as JSON
        #return jsonify({'prediction': prediction.tolist()})
        return render_template("index.html",prediction_text="The House price prediction is {}".format(prediction[0]))

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)