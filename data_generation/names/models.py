from django.db import models

class AbstractName(models.Model):
    name = models.TextField(max_length=100)

    class Meta:
        abstract = True


class FirstName(AbstractName):
    is_male = models.BooleanField()


class LastName(AbstractName):
    
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        NEUTRAL = 'N'
    
    # in the database, only 'M', 'F' or 'N' is saved
    matching_gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.NEUTRAL,
    )

    def for_males(self):
        """Returns true if the name is correct for males"""
        return self.matching_gender in {self.Gender.MALE, self.Gender.NEUTRAL}

    def for_females(self):
        """Returns true if the name is correct for females"""
        return self.matching_gender in {self.Gender.FEMALE, self.Gender.NEUTRAL}
