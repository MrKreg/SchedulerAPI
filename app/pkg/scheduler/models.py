from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.pkg.scheduler.choices import LessonType, Weekdays


class Lesson(models.Model):
    day = models.PositiveSmallIntegerField(_('weekday'), choices=Weekdays.choices(), default=Weekdays.MONDAY.value)
    weeks = ArrayField(
        verbose_name=_('weeks'),
        base_field=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)]),
        size=4,
        default=list
    )

    info = models.ForeignKey('info.LessonInfo', related_name='lessons', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(_('number'), validators=[MaxValueValidator(7)])
    classroom = models.ForeignKey('info.Classroom', related_name='lessons', on_delete=models.CASCADE)

    type = models.CharField(
        _('lesson type'),
        max_length=10,
        choices=LessonType.choices(),
        default=LessonType.LECTURE.value
    )

    @property
    def is_lecture(self):
        return self.type == LessonType.LECTURE.value

    @property
    def is_lab(self):
        return self.type == LessonType.LAB.value

    class Meta:
        ordering = ('day', 'number',)
        unique_together = ('day', 'number', 'weeks', 'classroom',)
