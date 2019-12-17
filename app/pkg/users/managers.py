from django.db.models import QuerySet, Manager

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
