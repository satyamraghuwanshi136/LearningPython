DAYS = 365
WEEKS = 52
MONTHS = 12

age = int(input("Enter your age: "))
years_remaning = 90 - age

user_days = DAYS*years_remaning
user_weeks = WEEKS*years_remaning
user_months = MONTHS*years_remaning

print(f"You have {user_days} days, {user_weeks} weeks and {user_months} months left")
