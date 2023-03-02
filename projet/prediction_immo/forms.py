from django import forms
from django.forms import ModelForm, DateInput, TimeInput, Select
from .models import predire_prix_maison
import pandas as pd

df = pd.read_csv("prediction_immo/df_kc_house_propre.csv")


class formulaire_prediction(ModelForm):
    class Meta:
        model = predire_prix_maison
        fields = ["bedrooms","bathrooms","sqft_living", "waterfront", "condition", "grade", "zipcode", "lat", "long"]
        widgets = {
            "waterfront" : Select(choices=[("0","0"), ("1","1")]),
            "condition" : Select(choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")]),
            "grade" : Select(choices=[("1","1"),("2","2"),("3","3"), ("4","4"),("5","5"),("6","6"), ("7","7"),("8","8"),("9","9"), ("10","10"),("11","11"),("12","12"),("13","13")]),
            "zipcode" : Select(choices=[(code, code) for code in sorted(df['zipcode'].unique())])
            }