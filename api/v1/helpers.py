from datetime import date, datetime


def get_birthday(iin: str) -> date:
    year = int(iin[:2])
    cur_year = datetime.now().year
    year = year + 2000 if cur_year < 100 else year + 1900
    month = int(iin[2:4])
    day = int(iin[4:6])
    return datetime(year, month, day).date()


def get_current_age(iin: str) -> int:
    birthday = get_birthday(iin)
    today = date.today()
    return today.year - birthday.year - (
        (today.month, today.day) < (birthday.month, birthday.day)
    )
