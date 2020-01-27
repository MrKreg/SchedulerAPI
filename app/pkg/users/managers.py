from django.contrib.auth.base_user import BaseUserManager
from django.db.models import QuerySet, Manager
from django.utils.translation import gettext_lazy as _

from app.pkg.users.choices import TgUserType


class TgQuerySet(QuerySet):

    def students(self):
        return self.filter(role=TgUserType.STUDENT.value)

    def teachers(self):
        return self.filter(role=TgUserType.TEACHER.value)


class TgManager(Manager):
    _queryset_class = TgQuerySet

    def students(self):
        return self.get_queryset().students()

    def teachers(self):
        return self.get_queryset().teachers()


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Enter the email'))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

