from datetime import datetime, timedelta
from collections import defaultdict 

def get_birthdays_per_week(users):
    arr = users
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    birthdays = defaultdict(list)

    def append_user(birthday):
        if today + timedelta(days = 1) <= birthday <= today + timedelta(days = 7):
            day_of_week = birthday.strftime('%A')

            if day_of_week in ['Saturday', 'Sunday']:
                if 'Monday' in birthdays.keys():
                    birthdays['Monday'].append(user['name'])
                else:
                    birthdays['Monday'] = [user['name']]
            else:
                birthdays[day_of_week].append(user['name'])

    for user in arr:
        try:
            # update year to current for comparison
            user['birthday'] = user['birthday'].replace(year=datetime.now().year)
        except ValueError:
            # if Feb 29th doesn't exist, set to 28th
            user['birthday'] = user['birthday'].replace(year=datetime.now().year, day=28)

        append_user(user['birthday'])
    
    for day, users in birthdays.items():
        print(f"{day}: {', '.join(users)}")

get_birthdays_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 10, 26)}, {"name": "Bill Gates1", "birthday": datetime(1955, 10, 23)}])
