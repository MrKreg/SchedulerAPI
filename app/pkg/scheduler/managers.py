from django.db.models import QuerySet, Manager
from django.utils import timezone

from app.pkg.scheduler.utils import get_week_number_by_day


class ScheduleQuerySet(QuerySet):

    def day_by_tg_id(self, tg_id, dt):
        week = get_week_number_by_day(dt)
        day = dt.isoweekday()
        return self.filter(weeks__contains=[week], lessons__group__tg_info__telegram_id=tg_id, day=day).order_by('number')

    def today_by_tg_id(self, tg_id):
        return self.day_by_tg_id(tg_id, timezone.now().today())


class ScheduleManager(Manager):
    _queryset_class = ScheduleQuerySet

    def day_by_tg_id(self, tg_id, dt):
        return self.get_queryset().day_by_tg_id(tg_id, dt)

    def today_by_tg_id(self, tg_id):
        return self.get_queryset().today_by_tg_id(tg_id)
