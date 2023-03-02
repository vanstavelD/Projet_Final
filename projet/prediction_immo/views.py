from django.shortcuts import render
from django.http import HttpResponse
from .forms import formulaire_prediction
import pandas as pd

# from .models import PredictionModel
# from sklearn.pipeline import Pipeline
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.neighbors import KNeighborsRegressor

# def home_page(request):
#     return render(request, 'home.html')


import pickle

# Charger le modèle entraîné avec pickle
with open('prediction_immo/trained_pipe.pkl', 'rb') as f:
    trained_pipe = pickle.load(f)

def prediction(request):
    if request.method == "POST":
        form = formulaire_prediction(request.POST)
        if form.is_valid():
            # Charger le modèle entraîné avec pickle
            with open('prediction_immo/trained_pipe.pkl', 'rb') as f:
                trained_pipe = pickle.load(f)

            # Récupérer les données soumises dans le formulaire
            data = form.cleaned_data
            bedrooms = data['bedrooms']
            bathrooms = data['bathrooms']
            sqft_living = data['sqft_living']
            waterfront = data['waterfront']
            condition = data['condition']
            grade = data['grade']
            zipcode = data['zipcode']
            lat = data['lat']
            long = data['long']

            # Créer un DataFrame avec les données soumises dans le formulaire
            input_data = pd.DataFrame({
                'bedrooms': [bedrooms],
                'bathrooms': [bathrooms],
                'sqft_living': [sqft_living],
                'waterfront': [waterfront],
                'condition': [condition],
                'grade': [grade],
                'zipcode': [zipcode],
                'lat': [lat],
                'long': [long]
            })

            # Faire la prédiction avec le modèle de machine learning
            predicted_price = trained_pipe.predict(input_data)[0]
            return render(request, 'home.html', {'form': form , 'predict' : predicted_price})

    # Rediriger l'utilisateur vers la page home si aucune prédiction n'a été faite
    form = formulaire_prediction()
    return render(request, 'home.html', {'form': form})

