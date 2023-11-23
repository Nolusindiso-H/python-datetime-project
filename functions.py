from dateutil import relativedelta
import datetime

def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days
    # 90 is passed in as a parameter from menus.py
    # Template:
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    print("Upcoming Birthdays function")
    print(people_list)
    pass


def display_age(person):
    # TODO: write code to display the age of person
    # Template:
    format_string = "%Y-%m-%d"
    birthday_dt = datetime.datetime.strptime(person['birthday'], format_string)
    today = datetime.date.today()

    difference = relativedelta.relativedelta(today,birthday_dt)
    # print(difference)
    print(f"{person['name']} is {difference.years} years, {difference.months}months, and {difference.days} days old")
    # print(person)
    # pass


def display_age_difference(people):
    # TODO: write the code to display the age difference between people
    # Template:
    # PERSON is older
    # PERSON and PERSON's age difference is: X years, X months, and X days

    print(people)
    pass
