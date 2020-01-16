import datetime

from django.db.models import QuerySet, Manager


class TermQuerySet(QuerySet):
    def get_by_date(self, dt):
        return self.filter(start__lte=dt, end__gte=dt).first()


class TermManager(Manager):
    _queryset_class = TermQuerySet

    def get_by_date(self, dt):
        return self.get_queryset().get_by_date(dt)

    def current(self):
        today = datetime.date.today()
        return self.get_by_date(today)
