from django.db import models
from django.utils.translation import ugettext_lazy as _


class Term(models.Model):
    start = models.DateField(_('term start date'))
    end = models.DateField(_('term end date'))


class Teacher(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    middle_name = models.CharField(_('middle name'), max_length=100)

    @property
    def initials(self):
        return '{} {}. {}.'.format(self.last_name, self.first_name[:1], self.middle_name[:1])


class Subject(models.Model):
    name = models.CharField(_('subject name'), max_length=100)


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='main_lessons', on_delete=models.CASCADE)
    second_teacher = models.ForeignKey(
        Teacher, related_name='second_lessons', on_delete=models.CASCADE, null=True
    )

    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.CASCADE)
    group = models.ForeignKey('users.Group', related_name='lessons', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='lessons', on_delete=models.CASCADE)


class Classroom(models.Model):
    floor = models.PositiveSmallIntegerField()
    block = models.CharField(max_length=10)
    number = models.PositiveSmallIntegerField()

    @property
    def info(self):
        return '{} {}{}'.format(self.block, self.floor, self.number)
