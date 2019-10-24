from app.pkg.common.choices import CharEnum, IntEnum


class LessonType(CharEnum):
    LECTURE = 'lecture'
    LAB = 'lab'


class Weekdays(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
