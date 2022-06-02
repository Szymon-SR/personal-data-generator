import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from addresses.models import PostAddress, Street

# tutaj home view, gdzie jest opis projektu i przycisk generuj,
# który zabiera nas do generacji

def home_view(request):
    return HttpResponse(render_to_string('home-view.html', {}))

def generation_view(request):
    post_ids = PostAddress.objects.values_list('id', flat=True)
    random_post_id = random.choice(post_ids)
    
    postaddr_obj = PostAddress.objects.get(id=random_post_id)

    street_ids = Street.objects.values_list('id', flat=True)
    random_street_id = random.choice(street_ids)

    street_obj = Street.objects.get(id=random_street_id)

    context = {
        'street_name': street_obj.name,
        'post_code': postaddr_obj.post_code,
        'city': postaddr_obj.city,
        'county': postaddr_obj.county,
        'voivodeship': postaddr_obj.voivodeship
    }

    HTML_STRING = render_to_string('generation-view.html', context=context)

    return HttpResponse(HTML_STRING)