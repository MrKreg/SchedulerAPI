# Generated by Django 2.1.4 on 2018-12-25 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulerapp', '0002_auto_20181223_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default='Mo', max_length=80),
        ),
    ]
