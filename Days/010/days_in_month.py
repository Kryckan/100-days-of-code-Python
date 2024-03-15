def is_leap(year: int) -> bool:
    """Check if a year is a leap year or not.

    Args:
        year (int): the year to be checked

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year: int, month: int):
    """Get the number of days in a given month of a year.

    Args:
        year (int): the year of the month
        month (int): the month for which to get the number of days

    Returns:
        Union[str, int]:
            - An integer representing the number of days in the month
              if the month is valid and the year is a leap year or not.
            - A string indicating that the month is invalid if the month is less than 1 or greater than 12.
    """
    # Number of days in each month (not considering leap years)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the month is invalid
    if month < 1 or month > 12:
        return "Invalid month"

    # Check if the year is a leap year and the month is February
    if month == 2 and is_leap(year):
        return 29

    # Return the number of days in the month
    return month_days[month - 1]


# Get user input for year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Call the days_in_month function to get the number of days in the month
days = days_in_month(year, month)

# Print the number of days in the month
print(days)
