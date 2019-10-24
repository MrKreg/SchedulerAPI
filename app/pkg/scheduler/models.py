from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeFramedModel

from app.pkg.scheduler.choices import LessonType, Weekdays
from app.pkg.scheduler.constants import ALL_WEEKS


class Schedule(TimeFramedModel):
    is_active = models.BooleanField(_('is active'), default=False)


class Lesson(models.Model):
    day = models.PositiveSmallIntegerField(choices=Weekdays.choices(), default=Weekdays.MONDAY.value)
    week = ArrayField(
        models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)]),
        size=4,
        default=ALL_WEEKS
    )

    info = models.ForeignKey('info.LessonInfo', related_name='lessons', on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, related_name='lessons', on_delete=models.CASCADE)

    number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(7)])
    classroom = models.CharField(max_length=10)

    type = models.CharField(max_length=10, choices=LessonType.choices(), default=LessonType.LECTURE.value)

    @property
    def is_lecture(self):
        return self.type == LessonType.LECTURE.value

    @property
    def is_lab(self):
        return self.type == LessonType.LAB.value

    class Meta:
        ordering = ('day', 'number',)
        unique_together = ('day', 'number', 'week', 'classroom',)
