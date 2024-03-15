age = input("What is your current age? ")

age_days = (90 - int(age)) * 365
age_weeks = (90 - int(age)) * 52
age_months = (90 - int(age)) * 12

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")
