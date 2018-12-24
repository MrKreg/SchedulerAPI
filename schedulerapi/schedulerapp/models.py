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
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
    )
    day = models.CharField(max_length=80, choices=DAYS, default='Mo')
    number = models.IntegerField()
    teacher = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    week = models.PositiveIntegerField(default=0)
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
