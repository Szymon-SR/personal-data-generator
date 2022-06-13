"""Views for our web application"""

from django.http import HttpResponse
from django.template.loader import render_to_string

from .forms import GenerationForm, ToFileForm
from .exporting import FileExporter
from .person_creation import generate_person_dict
from non_database import photo_request


def home_view(request):
    """View for the main page of the website"""

    # refresh the photo of the person
    photo_request.save_generated_photo()

    # render html
    return HttpResponse(render_to_string("home-view.html", {}))


def about_view(request):
    """View for the 'about' page of the website, with some information"""

    # render html with empty context
    return HttpResponse(render_to_string("about-view.html", {}))


def generation_view(request):
    """View for generating one person"""

    # initializing a form object to get input from user
    form = GenerationForm(request.GET or None)
    form.fields["gender"].initial = "both"
    form.fields["minimal_age"].initial = 18
    form.fields["maximal_age"].initial = 100

    # by default, generate female and male names
    form_gender = "both"
    form_min_age = 18
    form_max_age = 100

    if request.method == "GET" and form.is_valid():
        form_gender = form.cleaned_data["gender"]
        # gender is' both', 'female' or 'male'
        form_min_age = form.cleaned_data["minimal_age"]
        form_max_age = form.cleaned_data["maximal_age"]

    # use a function generating all the data needed
    person_data = generate_person_dict(
        requested_gender=form_gender,
        all_values_requested=True,
        min_age=form_min_age,
        max_age=form_max_age,
    )

    context = {
        "form": form,
    }
    # add the personal data to context
    context.update(person_data)

    # render html
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

        # create a list to store multiple dictionaries, each with data of one person
        all_people = [
            generate_person_dict(requested_values=form.cleaned_data)
            for _ in range(form_number_of_rows)
        ]

        base_filename = "personal_data."
        exporter = FileExporter(all_people)

        # set file name and use function to export data
        if form_datatype == "txt":
            filepath = exporter.export_data_to_txt()
            filename = f"{base_filename}txt"
        elif form_datatype == "csv":
            filepath = exporter.export_data_to_csv()
            filename = f"{base_filename}csv"
        elif form_datatype == "excel":
            filepath = exporter.export_data_to_excel()
            filename = f"{base_filename}xlsx"

        # previous functions created a file and returned a path, retrieve this file by path and serve to user
        with open(filepath, "rb") as f:
            file = f.read()
            response = HttpResponse(file)
            if form_datatype == "excel":
                response[
                    "Content-Type"
                ] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            response["Content-Disposition"] = f"attachment; filename={filename}"

            return response

    context = {
        "form": form,
    }

    HTML_STRING = render_to_string("file-view.html", context=context)

    return HttpResponse(HTML_STRING)
