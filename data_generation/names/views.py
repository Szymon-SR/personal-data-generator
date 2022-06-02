from django.shortcuts import render
from .models import FirstName, LastName

def first_name_create_view(request):
    # creating a new object
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')
        is_male = request.POST.get('is_male')

        first_name_obj = FirstName.objects.create(name=name, is_male=is_male)

        context['object'] = first_name_obj
        context['created'] = True

    # return render()

def last_name_create_view(request):
    # creating a new object
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')
        matching_gender = request.POST.get('matching_gender')

        last_name_obj = LastName.objects.create(name=name, matching_gender=matching_gender)

        context['object'] = last_name_obj
        context['created'] = True

    # return render()
