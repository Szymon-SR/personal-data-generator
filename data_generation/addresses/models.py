from django.db import models

class PostAddress(models.Model):
    city = models.TextField()
    post_code = models.TextField()
    voivodeship = models.TextField()
    county = models.TextField()