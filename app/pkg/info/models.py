from django.db import models
from django.utils.translation import ugettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    middle_name = models.CharField(_('middle name'), max_length=100)

    @property
    def initials(self):
        return f'{self.last_name} {self.first_name[:1]}. {self.middle_name[:1]}.'


class Subject(models.Model):
    name = models.CharField(_('subject name'), max_length=100)


class LessonInfo(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='lessons_info', on_delete=models.CASCADE)
    second_teacher = models.ForeignKey(
        Teacher, related_name='lessons_info', on_delete=models.CASCADE, null=True
    )

    subject = models.ForeignKey(Subject, related_name='lessons_info', on_delete=models.CASCADE)
    group = models.ForeignKey('users.Group', related_name='lessons_info', on_delete=models.CASCADE)


class Classroom(models.Model):
    floor = models.PositiveSmallIntegerField(null=True)
    block = models.CharField(max_length=10)
    number = models.PositiveSmallIntegerField()

    @property
    def info(self):
        return f'{self.block}{self.floor}{self.number}'
