from django.db import models


class RecognitionResult(models.Model):
    material_type = models.CharField(max_length=100)
    confidence = models.FloatField()
    image = models.ImageField(upload_to='media')
