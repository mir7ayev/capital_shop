from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_solved')
    list_display_links = ('id', 'name')
