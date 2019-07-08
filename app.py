import random
import pandas as pd
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.pipeline import Pipeline
import joblib
from flask import Flask, request, render_template, jsonify


#Load Model 1: Classification - Probability of Default
class_model = joblib.load('nn_v7.joblib')
#Load Model 2: Regression - Annualized Return
regr_model = joblib.load('ridge_lin_reg_v2.joblib')

app = Flask(__name__, static_url_path="")

@app.route('/') #home page
def index():
    """Return the main page."""
    return render_template('index.html')


# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     """Return a random prediction."""
#     data = request.json
#     prob_def_prediction = 1-class_model.predict_proba([data['user_input']])
#     return_prediction = regr_model.predict(data['user_input'])
#     return jsonify({'probability_of_default': prob_def_prediction},
#                     {'predicted_annualized_return': return_prediction})

