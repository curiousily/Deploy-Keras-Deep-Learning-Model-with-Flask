# Zero to Production

> It is not recommended to deploy your production models as shown here. This is just an end-to-end example to get started quickly.

This guide shows you how to:

- build a Deep Neural Network that predicts Airbnb prices in NYC (using scikit-learn and Keras)
- build a REST API that predicts prices based on the model (using Flask and gunicorn)
- deploy the model to production on Google App Engine

# Quick start

Requirements:

- Python 3.7
- Google Cloud Engine account

```bash
git clone git@github.com:curiousily/End-to-End-Machine-Learning-with-Keras.git
cd End-to-End-Machine-Learning-with-Keras
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Start local server

```bash
flask run
```

## Make predictions

```bash
curl -d '{"neighbourhood_group": "Brooklyn", "latitude": 40.64749, "longitude": -73.97237, "room_type": "Private room", "minimum_nights": 1, "number_of_reviews": 9, "calculated_host_listings_count": 6, "availability_365": 365}' -H "Content-Type: application/json" -X POST http://localhost:5000
```

## Deploy to Google App Engine

```bash
gcloud app deploy
```
