import random
from enum import Enum
from django.http import HttpResponse
from django.template.loader import render_to_string

from addresses.models import PostAddress, Street
from names.models import FirstName, LastName

from non_database import number_generator

from .forms import GenerationForm

class GenderLetter(Enum):
        MALE = 'M'
        FEMALE = 'F'
        NEUTRAL = 'N'

def home_view(request):
    """View for the main page of the website"""
    
    return HttpResponse(render_to_string('home-view.html', {}))


def generation_view(request):
    """View for generating one person"""

    # initializing a form object to get input from user
    form = GenerationForm(request.GET or None)
    form.fields['gender'].initial = 'both'

    # by default, generate female and male names
    form_gender='both'

    # print(request.path)

    if request.method == 'GET' and form.is_valid():
        form_gender = form.cleaned_data['gender']   # gender is' both', 'female' or 'male'
        print(form_gender)

    # convert text gender to boolean (True if male, False if female)
    # if user picked both genders, randomize it
    gender_to_boolean = {'both': random.choice([True, False]), 'female': False, 'male': True}
    male_requested = gender_to_boolean[form_gender]

    first_name_ids = FirstName.objects.filter(is_male=male_requested).values_list('id', flat=True)
    first_name_obj = FirstName.objects.get(id=random.choice(first_name_ids))

    # both genders can take neutral last names, pick a letter to exclude
    boolean_to_excluded_gender = {True: 'F', False: 'M'}

    last_name_ids = LastName.objects.exclude(matching_gender=boolean_to_excluded_gender[male_requested]).values_list('id', flat=True)
    last_name_obj = LastName.objects.get(id=random.choice(last_name_ids))

    # NUMBERS
    pesel_gen = number_generator.PeselGenerator(male_requested)

    # ADDRESS
    post_ids = PostAddress.objects.values_list('id', flat=True)    
    postaddr_obj = PostAddress.objects.get(id=random.choice(post_ids))

    street_ids = Street.objects.values_list('id', flat=True)
    street_obj = Street.objects.get(id=random.choice(street_ids))

    context = {
        'form': form,
        'first_name': first_name_obj.name.title(),
        'last_name': last_name_obj.name,
        'phone_number': number_generator.generate_phone_number(),
        'birth_date': pesel_gen.get_formatted_birth_date(),
        'pesel': pesel_gen.pesel,
        'street_name': street_obj.name,
        'post_code': postaddr_obj.post_code,
        'city': postaddr_obj.city,
        'county': postaddr_obj.county,
        'voivodeship': postaddr_obj.voivodeship,
        'house_number': number_generator.generate_house_number(),
    }

    HTML_STRING = render_to_string('generation-view.html', context=context)

    return HttpResponse(HTML_STRING)


def file_view(request):
    """View for generating multiple people and exporting to a file"""
    context = {}
    HTML_STRING = render_to_string('file-view.html', context=context)

    return HttpResponse(HTML_STRING)