from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=8)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class User(models.Model):
    telegram_id = models.IntegerField()
    group = models.ForeignKey(
        Group,
        related_name='users',
        on_delete=models.CASCADE,
    )
