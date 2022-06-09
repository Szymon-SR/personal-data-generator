import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from addresses.models import PostAddress, Street
from names.models import FirstName, LastName

from non_database import number_generator

def home_view(request):
    """View for the main page of the website"""
    
    return HttpResponse(render_to_string('home-view.html', {}))


def generation_view(request):
    """View for generating one person"""

    # picking person gender, male or female
    generating_male = random.choice([True, False])

    first_name_ids = FirstName.objects.filter(is_male=generating_male).values_list('id', flat=True)
    first_name_obj = FirstName.objects.get(id=random.choice(first_name_ids))

    incorrect_gender = {True: 'F', False: 'M'}

    last_name_ids = LastName.objects.exclude(matching_gender=incorrect_gender[generating_male]).values_list('id', flat=True)
    last_name_obj = LastName.objects.get(id=random.choice(last_name_ids))

    # NUMBERS
    pesel_gen = number_generator.PeselGenerator(generating_male)

    # ADDRESS
    post_ids = PostAddress.objects.values_list('id', flat=True)    
    postaddr_obj = PostAddress.objects.get(id=random.choice(post_ids))

    street_ids = Street.objects.values_list('id', flat=True)
    street_obj = Street.objects.get(id=random.choice(street_ids))

    context = {
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