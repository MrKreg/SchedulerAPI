from django.contrib import admin

from app.pkg.info.models import Teacher


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    search_fields = ('last_name', 'first_name', 'middle_name')
