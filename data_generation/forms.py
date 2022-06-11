"""Forms to use in our web app to get input from the user. There are used both in generating a single person and generating to a file."""

from django import forms

GENDER_CHOICES = (
    ("both", "Female or male"),
    ("female", "Female"),
    ("male", "Male"),
)


class GenerationForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating one person"""

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, label="Gender to generate", initial="both"
    )
    minimal_age = forms.IntegerField(max_value=200, min_value=1, label="Minimal age")
    maximal_age = forms.IntegerField(max_value=200, min_value=1, label="Maximal age")

    def clean(self):
        """Clean function is included in forms.Form, i override it to check that provided minimal age is smaller than maximal age"""
        # use forms.Form clean first
        cleaned_data = super().clean()
        minimal_age = cleaned_data.get("minimal_age")
        maximal_age = cleaned_data.get("maximal_age")

        # check if minimal_age and maximal_age are correct
        if minimal_age and maximal_age:
            if minimal_age > maximal_age:
                raise forms.ValidationError(
                    "Maximal age has to be greater than minimal age."
                )


# possible choices to pick a file type
FILE_CHOICES = (("txt", "TXT file"), ("csv", "CSV file"), ("excel", "EXCEL file"))


class ToFileForm(forms.Form):
    """Django Form used to generate html forms, used to set parameters in generating data to file"""

    # number of rows is number of people generated
    number_of_rows = forms.IntegerField(
        max_value=1000, min_value=1, label="Number of people to generate"
    )
    file_type = forms.ChoiceField(
        choices=FILE_CHOICES, label="Type of file", initial="txt"
    )

    # following are tick boxes, they tell us which data user wants
    gen_first_name = forms.BooleanField(
        label="First name", initial=True, required=False
    )
    gen_last_name = forms.BooleanField(label="Last name", initial=True, required=False)
    gen_phone = forms.BooleanField(label="Phone number", initial=True, required=False)
    gen_birth = forms.BooleanField(label="Birth date", initial=True, required=False)
    gen_pesel = forms.BooleanField(label="PESEL number", initial=True, required=False)
    gen_street = forms.BooleanField(label="Street", initial=True, required=False)
    gen_house_number = forms.BooleanField(
        label="House / apartment number", initial=True, required=False
    )
    gen_post_code = forms.BooleanField(label="Post code", initial=True, required=False)
    gen_city = forms.BooleanField(label="City / Town", initial=True, required=False)
    gen_county = forms.BooleanField(label="County", initial=True, required=False)
    gen_voivodeship = forms.BooleanField(
        label="Voivodeship", initial=True, required=False
    )
