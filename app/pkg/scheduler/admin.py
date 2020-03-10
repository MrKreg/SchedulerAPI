from django.contrib import admin
from app.pkg.scheduler.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'number', 'get_lesson_name', 'type', 'get_teacher', 'get_classroom')
    list_filter = ('day', 'number', 'classroom')
    search_fields = ('info__teacher__first_name', 'info__teacher__last_name', 'info__subject__name')
    ordering = ('day', 'number')

    def get_lesson_name(self, obj):
        return obj.info.subject.name

    get_lesson_name.short_description = 'Lesson'

    def get_teacher(self, obj):
        return obj.info.teacher.initials

    get_teacher.short_description = 'Teacher'

    def get_classroom(self, obj):
        return obj.classroom.info

    get_classroom.short_description = 'Classroom'
