from datetime import datetime
from datetime import timedelta


def date_input_there(number):
    today = datetime.now()
    need_date = datetime.strftime(today + timedelta(days=number), "%d.%m.%Y")
    print(need_date)
    return need_date


def date_input_back(number):
    today = datetime.now()
    need_date = datetime.strftime(today + timedelta(days=number), "%d.%m.%Y")
    print(need_date)
    return need_date

