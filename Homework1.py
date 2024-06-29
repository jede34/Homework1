# from datetime import datetime


# get_days_from_today = datetime(year=2020, month=10, day=9)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - get_days_from_today.toordinal()
# print(days_since)


import datetime

def get_days_from_today(date):
    specific_date = datetime.datetime(year=2020, month=10, day=9)
    current_date = datetime.datetime.now()
    days_since = (current_date - specific_date).days
    return days_since


days_since = get_days_from_today(datetime.datetime.now())
print(f"Days since specific date: {days_since}")

    