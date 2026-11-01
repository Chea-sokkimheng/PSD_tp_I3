#PROBLEM 6
def is_leap(year):
   return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month"
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

for year in [2020, 2021, 2022, 2023, 2024]:

    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

print("Feb 2024: ", days_in_month(2024, 2),
      "| Feb 2026:", days_in_month(2026, 2),
      "| Apr :", days_in_month(2023, 4),
      "| month 13 :", days_in_month(2023, 13))

count = 0

for year in range(2000, 2101):
    if is_leap(year):
        count += 1
print(f"Number of leap years from 2000 and 2100: {count}")
  