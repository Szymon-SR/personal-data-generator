from django.contrib import admin
from .models import PostAddress

class PostAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_code']
    search_fields = ['post_code', 'city']

admin.site.register(PostAddress, PostAddressAdmin)