from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=8, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(
        'Group',
        related_name='groups',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('id',)
    
    def __str__(self):
        return self.id

class Lesson(models.Model):
    DAYS = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )
    WEEKS = (
        (0, 'Всі'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, 'Непарні'),
        (6, 'Парні'),
    )
    day = models.CharField(max_length=80, choices=DAYS, default=1)
    number = models.IntegerField()
    teacher = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    week = models.IntegerField(default=0, choices=WEEKS)
    group = models.ForeignKey(
        'Group',
        related_name='lessons',
        on_delete=models.CASCADE,
    )
    classroom = models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        ordering = ('day','number',)
        unique_together = (('day','number','teacher','subject','week','group','classroom'),)

    def __str__(self):
        return self.subject
