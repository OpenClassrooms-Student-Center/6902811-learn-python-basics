from main import monthly_salary, weekly_salary, hourly_wage

def test_monthly_salary():
    input = 12000
    expected_output = 1000.0
    assert monthly_salary(input) == expected_output, "The function monthly_salary does not correctly divide the annual salary by 12."

def test_weekly_salary():
    input = 4000
    expected_output = 1000
    assert weekly_salary(input) == expected_output, "The function weekly_salary does not correctly divide the monthly salary by 4."

def test_hourly_wage():
    weekly_salary = 1000
    hourly = 10
    expected_output = 100
    assert hourly_wage(weekly_salary, hourly) == expected_output, "The function hourly_salary does not correctly divide the weekly salary by the number of hours worked per week."