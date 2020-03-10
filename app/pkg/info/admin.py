from django.contrib import admin

from app.pkg.info.models import Teacher, Term, Subject, Classroom, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    search_fields = ('last_name', 'first_name', 'middle_name')
    ordering = ('last_name', 'first_name',)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('start', 'end')
    ordering = ('-start',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('info',)
    list_filter = ('floor', 'block', 'number')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'second_teacher', 'subject', 'group', 'term')
