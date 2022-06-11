from .models import PostAddress, Street

def post_address_create_view(request):
    """View for creating a new post address object"""
    context = {}

    if request.method == "POST":
        city = request.POST.get('city')
        post_code = request.POST.get('post_code')
        voivodeship = request.POST.get('voivodeship')
        county = request.POST.get('county')

        post_address_obj = PostAddress.objects.create(city=city, post_code=post_code, voivodeship=voivodeship, county=county)

        context['object'] = post_address_obj
        context['created'] = True


def street_address_create_view(request):
    """View for creating a new street object"""
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')

        street_obj = Street.objects.create(name=name)

        context['object'] = street_obj
        context['created'] = True
