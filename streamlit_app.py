from flask import Flask, render_template, request, jsonify
import joblib
import pickle

app = Flask(__name__)

# Load the saved model
model = joblib.load('multioutput_xgboost_model_redefined.pkl')

@app.route('/')
def home():
    # return 'fuck jinja2'
    return render_template('index.html')  # Create an HTML template for your website

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        # Get input data from the website's form or API request
        input1 = float(request.form['quantity'])
        input2 = float(request.form['quantity'])
        # print(input1)
        # print(input2)
        # input_data=(input1,input2).toarray()
        # input_data = request.form  # Adjust this based on your website's form structure
        # input_data=[[input1,input2]]

        # Preprocess the input data if needed

        # Make predictions using the loaded model
        predictions = model.predict([[input1,input2]])
        if (((predictions[:,0]<8.5) and (predictions[:,0]>6.5)) and (predictions[:,14]<1300)):
            return "Your pH level of water is {} while your TDS content is {} and therefore the water quality is good for drinking".format(predictions[:,0],predictions[:,14])
        else:
            return "pH level is {} while your TDS content is {}, and hence not safe for drinking".format(predictions[:,0],predictions[:,14])

        # You can process the predictions further if necessary
        # return predictions
        # Return the predictions as JSON
        # return jsonify({'your pH is:-': predictions.tolist()})
    except Exception as e:
        return 'error'
        # return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 