"""Django models connected to people's name data"""

from django.db import models

class AbstractName(models.Model):
    """Abstract model representing a name"""
    name = models.TextField(max_length=100)

    class Meta:
        # we set abstract to True, this model can't have objects
        # and can't exist in the database
        abstract = True

    # abstract name is not correct for either males or females
    def for_females(self):
        return False

    def for_males(self):
        return False


class FirstName(AbstractName):
    """Model inheriting from abstract name, representing first name"""

    is_male = models.BooleanField()

    def for_females(self):
        """Returns true if the name is correct for females"""
        return not self.is_male

    def for_males(self):
        """Returns true if the name is correct for males"""
        return self.is_male


class LastName(AbstractName):
    """
    Model inheriting from abstract name, representing first name.
    They are represented differently, because first names can be either male or female
    And last names can also be gender neutral
    """


    class Gender(models.TextChoices):
        """Class to provide options for text choices field"""
        MALE = 'M'
        FEMALE = 'F'
        NEUTRAL = 'N'

    # in the database, only 'M', 'F' or 'N' is saved
    matching_gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.NEUTRAL,
    )

    def for_females(self):
        """Returns true if the name is correct for females"""
        return self.matching_gender in {self.Gender.FEMALE, self.Gender.NEUTRAL}

    def for_males(self):
        """Returns true if the name is correct for males"""
        return self.matching_gender in {self.Gender.MALE, self.Gender.NEUTRAL}
