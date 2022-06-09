from django import forms

GENDER_CHOICES = (
    ('both', 'Female or male'),
    ('female', 'Female'),
    ('male', 'Male'),
)

class GenerationForm(forms.Form):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender to generate', initial='both')

    def clean_gender(self):
        if not self['gender'].html_name in self.data:
            return self.fields['gender'].initial
        return self.cleaned_data['gender']