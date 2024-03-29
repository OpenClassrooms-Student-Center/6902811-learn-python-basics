# Context

You need to create a program that calculates an employee's hourly wage based on their monthly salary and the number of hours they work per week. The program should use functions to perform the calculations.

# Instructions

1. **Create** a function called `monthly_salary(annual_salary)` which takes an **annual salary** as a *parameter* and *returns* the corresponding **monthly salary** by **dividing** the annual salary by *12*. *(Copy-paste the function name to avoid test failures)*
2. **Create** a function called `weekly_salary(monthly_salary)` which takes a **monthly salary** as a parameter and *returns* the corresponding **weekly salary** by **dividing** the monthly salary by *4*. *(Copy-paste the function name to avoid test failures)*
3. **Create** a function called `hourly_wage(weekly_salary, hours_worked)` which takes a **weekly salary** and the **number of hours worked per week** as *parameters*, and *returns* the corresponding **hourly wage** by **dividing** the weekly salary by the number of hours worked per week. *(Copy-paste the function name to avoid test failures)*
4. **Create** a `main` function to *call* the functions:
   * **Ask** the user to **input** their *annual salary*.
   * **Ask** the user to **input** the *number of hours worked per week*.
   * **Call** the previously created functions to calculate the corresponding hourly wage.
   * **Display** the result in the format: `"Your hourly wage is XX euros"`.

