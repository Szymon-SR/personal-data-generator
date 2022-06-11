"""Django models connected to address data"""

from django.db import models


class PostAddress(models.Model):
    """Real place based on polish post code, containing other names of locations of particular post code"""

    city = models.TextField()
    post_code = models.TextField()
    voivodeship = models.TextField()
    county = models.TextField()


class Street(models.Model):
    """Street name model, containing one of the real street names in Poland"""

    name = models.TextField()
