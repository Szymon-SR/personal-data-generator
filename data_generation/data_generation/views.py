
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string

from .forms import GenerationForm, ToFileForm
from .exporting import export_data_to_csv, export_data_to_txt
from .person_creation import generate_person_dict


def home_view(request):
    """View for the main page of the website"""

    return HttpResponse(render_to_string("home-view.html", {}))


def generation_view(request):
    """View for generating one person"""

    # initializing a form object to get input from user
    form = GenerationForm(request.GET or None)
    form.fields["gender"].initial = "both"

    # by default, generate female and male names
    form_gender = "both"

    if request.method == "GET" and form.is_valid():
        form_gender = form.cleaned_data[
            "gender"
        ]  # gender is' both', 'female' or 'male'

    person_data = generate_person_dict(form_gender, all_values_requested=True)

    context = {
        "form": form,
    }
    # add the personal data to context
    context.update(person_data)

    HTML_STRING = render_to_string("generation-view.html", context=context)

    return HttpResponse(HTML_STRING)


def file_view(request):
    """View for generating multiple people and exporting to a file"""

    # initializing a form object to get input from user
    form = ToFileForm(request.GET or None)
    form.fields["number_of_rows"].initial = 10

    if request.method == "GET" and form.is_valid():
        form_number_of_rows = form.cleaned_data["number_of_rows"]
        form_datatype = form.cleaned_data["file_type"]

        print(form.cleaned_data)

        # create a list to store multiple dictionaries, each with data of one person
        all_people = [
            generate_person_dict(requested_values=form.cleaned_data)
            for _ in range(form_number_of_rows)
        ]

        if form_datatype == "txt":
            filepath = export_data_to_txt(all_people)
            filename = "personal_data.txt"
        else:
            filepath = export_data_to_csv(all_people)
            filename = "personal_data.csv"

        file = open(filepath).read()
        response = FileResponse(file)
        response["Content-Disposition"] = f"attachment; filename={filename}"

        return response

    context = {
        "form": form,
    }

    HTML_STRING = render_to_string("file-view.html", context=context)

    return HttpResponse(HTML_STRING)
