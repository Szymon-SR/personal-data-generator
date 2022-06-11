from django.contrib import admin
from .models import FirstName, LastName


class FirstNameAdmin(admin.ModelAdmin):
    """Defines admin panel for first name model"""

    list_display = ["id", "name"]
    search_fields = ["name", "is_male"]


class LastNameAdmin(admin.ModelAdmin):
    """Defines admin panel for last name model"""

    list_display = ["id", "name"]
    search_fields = ["name", "matching_gender"]


admin.site.register(FirstName, FirstNameAdmin)
admin.site.register(LastName, LastNameAdmin)
