# campusApp/admin.py
from django.contrib import admin
from .models import UniversityCampus

# Register UniversityCampus so we can manage campuses in the admin interface
@admin.register(UniversityCampus)
class UniversityCampusAdmin(admin.ModelAdmin):
    # Display these columns in the list view
    list_display = ('campus_name', 'state', 'campus_id')
