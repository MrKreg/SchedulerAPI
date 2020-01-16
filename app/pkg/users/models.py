from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.pkg.users.choices import TgUserType
from app.pkg.users.managers import TgManager


class Group(models.Model):
    speciality_part = models.CharField(_('shorted speciality name'), max_length=2)
    year = models.PositiveIntegerField(_('entry year'))
    number = models.PositiveSmallIntegerField(_('group number'))

    @property
    def name(self):
        return '{}-{:02d}-{:02d}'.format(self.speciality_part, self.year, self.number)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    USERNAME_FIELD = 'email'


class TgBotInfo(models.Model):
    first_name = models.CharField(_("user's telegram first name"), max_length=100, null=True)
    last_name = models.CharField(_("user's telegram last name"), max_length=100, null=True)
    username = models.CharField(_("user's telegram username"), max_length=100, null=True, unique=True)
    telegram_id = models.PositiveIntegerField(_('telegram user id'), unique=True)
    role = models.CharField(
        _('role'), max_length=20, choices=TgUserType.choices(), default=TgUserType.STUDENT.value,
        db_index=True
    )
    group = models.ForeignKey(
        Group, related_name='tg_info', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = _('telegram bot info')
        verbose_name_plural = _('telegram bot info')

    objects = TgManager

    @property
    def is_student(self):
        return self.role == TgUserType.STUDENT.value

    @property
    def is_teacher(self):
        return self.role == TgUserType.TEACHER.value
