#Task 1

from datetime import datetime

def previous_date() -> datetime:
    while True:
        date_input = input("Enter date in format YYYY-MM-DD: ")
        try:
            previous_date = datetime.strptime(date_input, "%Y-%m-%d")
            return previous_date
        except ValueError:
            print("Date must be inputed in YYYY-MM-DD format. Try again")

date = previous_date()

def get_days_from_today(date: datetime) -> datetime:
    current_date = datetime.today()
    diff_between_dates = current_date - date
    return diff_between_dates

print(f"Кількість днів між заданою датою й поточною датою: {get_days_from_today(date)}")