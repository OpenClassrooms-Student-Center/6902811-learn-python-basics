# Definition of the function monthly_salary
def monthly_salary(annual_salary):
    return annual_salary / 12


# Definition of the function weekly_salary
def weekly_salary(monthly_salary):
    return monthly_salary / 4


# Definition of the function hourly_wage
def hourly_wage(weekly_salary, hours_worked):
    return weekly_salary / hours_worked


def main():
    # Ask the user to enter their annual salary.
    annual_salary = float(input("Enter your annual salary : "))
    # Ask the user to enter the number of hours worked per week.
    hours_worked = float(input("Enter the number of hours worked per week : "))

    # Hourly wage calculation
    monthly = monthly_salary(annual_salary)
    weekly = weekly_salary(monthly)
    hourly = hourly_wage(weekly, hours_worked)

    # Displaying the result
    print("Your hourly wage is",  hourly, "euros.")

if __name__ == "__main__":
    main()