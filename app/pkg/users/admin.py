from django.contrib import admin

from app.pkg.users.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
