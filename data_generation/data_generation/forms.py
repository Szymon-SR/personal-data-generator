from django import forms

GENDER_CHOICES = (
    ('both', 'Female or male'),
    ('female', 'Female'),
    ('male', 'Male'),
)

class GenerationForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating one person"""

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender to generate', initial='both')


FILE_CHOICES = (
    ('txt', 'TXT file'),
    ('csv', 'CSV file'),
)


class ToFileForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating data to file"""

    number_of_rows = forms.IntegerField(max_value=1000, min_value=1, label='Number of people to generate')
    file_type = forms.ChoiceField(choices=FILE_CHOICES, label='Type of file', initial='txt')
    
    gen_first_name = forms.BooleanField(label="First name", initial=True, required=False)
    gen_last_name = forms.BooleanField(label="Last name", initial=True, required=False)
    gen_phone = forms.BooleanField(label="Phone number", initial=True, required=False)
    gen_birth = forms.BooleanField(label="Birth date", initial=True, required=False)
    gen_pesel = forms.BooleanField(label="PESEL number", initial=True, required=False)
    gen_street = forms.BooleanField(label="Street", initial=True, required=False)
    gen_house_number = forms.BooleanField(label="House / apartment number", initial=True, required=False)
    gen_post_code = forms.BooleanField(label="Post code", initial=True, required=False)
    gen_city = forms.BooleanField(label="City / Town", initial=True, required=False)
    gen_county = forms.BooleanField(label="County", initial=True, required=False)
    gen_voivodeship = forms.BooleanField(label="Voivodeship", initial=True, required=False)
