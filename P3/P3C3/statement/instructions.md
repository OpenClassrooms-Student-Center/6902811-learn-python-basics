# Context

Suppose you are an HR manager and you need to create a file containing the salaries of your employees. We will read from a **CSV** file the names of the employees and the hours worked, and then **create** another **CSV file** with their *calculated salaries*.

# Instructions

1. **Write** a script to read the content of our file `input.csv` in the following format:

| name  | hours_worked |
| ------------- |:-------------:|
| Tavin Quickshadow      | **36**     |
| Elara Sunleaf      | **41**     |
| Mirelle Starwhisper      | **40**     |

**Tip**: Create an `extract()` function that returns the data from the `input.csv` file.

2. **Create** a new CSV file called `output.csv` which should have the following format:

* **Salaries** are calculated using the formula `hours_worked * 15`. *(Note: the keys should be lowercase for the tests to pass)*

| name  | salary |
| ------------- |:-------------:|
| Tavin Quickshadow      | **540**     |
| Elara Sunleaf      | **615**     |
| Mirelle Starwhisper      | **600**     |

**Tip**: Create a first function `transform()` which will be responsible for **transforming** the data and creating a new container with all the **new data**. And then a `load()` function that will load the new data into the `output.csv` file.
