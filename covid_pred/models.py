from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Database table creation
class CovidPrediction(models.Model):
    sex = models.IntegerField()
    intubed = models.IntegerField()
    pneumonia = models.IntegerField()
    age = models.IntegerField()
    diabetes = models.IntegerField()
    copd = models.IntegerField()
    asthma = models.IntegerField()
    hypertension = models.IntegerField()
    cardiovascular = models.IntegerField()
    obesity = models.IntegerField()
    renal_chronic = models.IntegerField()
    tobacco = models.IntegerField()
    contact_other_covid = models.IntegerField()
    icu = models.IntegerField()
    classification = models.IntegerField()

    def __int__(self):
        return self.age