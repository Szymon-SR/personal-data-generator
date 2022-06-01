from django.contrib import admin
from .models import PostAddress, Street

class PostAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_code']
    search_fields = ['post_code', 'city']

class StreetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

admin.site.register(PostAddress, PostAddressAdmin)
admin.site.register(Street, StreetAdmin)