from django import forms

GENDER_CHOICES = (
    ('both', 'Female or male'),
    ('female', 'Female'),
    ('male', 'Male'),
)

class GenerationForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating one person"""

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender to generate', initial='both')



class ToFileForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating data to file"""

    number_of_rows = forms.IntegerField(max_value=1000, min_value=1, label='Number of people to generate')