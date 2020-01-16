from app.pkg.info.models import Term


def get_week_number_by_day(date, next=False):
    term = Term.objects.current()
    _, cur_week, day = date.isocalendar()
    start_week = term and term.start.isoweekday() + next

    if not start_week:
        return 0

    return (cur_week - start_week) % 4 or 4
