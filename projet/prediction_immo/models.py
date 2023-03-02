from django.db import models


class predire_prix_maison(models.Model):
    
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    sqft_living = models.IntegerField()
    waterfront = models.BooleanField()
    condition = models.IntegerField()
    grade = models.IntegerField()
    zipcode = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    
    