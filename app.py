import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\Dell\\Documents\\internship\\env\\model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output<=20:
            return render_template('index.html', prediction_text='PERFORMANCE OF BATSMAN IS POOR WITH BATTING AVERAGE OF {}'.format(output))
    elif output<35:
        return render_template('index.html', prediction_text='PERFORMANCE OF BATSMAN IS AVERAGE WITH BATTING AVERAGE OF {}'.format(output))
    else:
        return render_template('index.html', prediction_text='PERFORMANCE OF BATSMAN IS EXECELLENT WITH BATTING AVERAGE OF {}'.format(output))
        
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)