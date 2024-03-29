# Context

You will create a calculator that will perform a simple operation between two numbers. So, you will need to create two variables to store the two numbers, and one variable to store the symbol representing the operation to be performed. You will first create a conditional structure that will check the validity of the variables and the symbol. Then, you will create a second conditional structure to perform the operation based on the chosen symbol. Don't worry, the exercise will be guided by questions. Let's get started! It's your turn to play!

# Instructions

#### 1. Create two variables `left_number` and `right_number`, and assign each of them an integer using an input.
- The value for **each variable** must be assigned using the `input()` function, which allows the user to enter a string of characters.

#### 2. Create a variable `operation` to store the operation symbol **(`+`, `-`, `*`, or `/`)**. The operator will also be requested using the `input()` function.

#### 3. Create one last variable `result` initialized to 0, which will then contain the calculation result.

#### 4. Check the two integer numbers

* Check that **both variables** `left_number` and `right_number` are indeed integers using the `isnumeric()` function.
* If one or both are not integers, display an error message accordingly and exit the program. Display the following message: `Error: both numbers must be integers` *(Copy and paste to prevent the test failed)*
* Otherwise, convert them to integers using the `int()` function.

#### 5. Check the symbol

* Check that the symbol stored in the `operation` variable corresponds to one of the 4 allowed operations (`+`, `-`, `*`, or `/`) using a `match` structure and perform the corresponding calculation in each case. Store the result in the `result` variable.
* If the symbol is not correct, display an error message accordingly and exit the program. (**Hint**: *think about the default value of the match case*) Display the following message: `Error: the operation symbol must be '+', '-', '*', or '/'.` *(Copy and paste to prevent the test failed)*
* It is impossible to divide a number by **0**, so an additional conditional structure is needed to check this case in the `match` structure. Use if-else conditions to perform this operation; if there is a division by 0, display `Error: division by zero is not allowed.`(Copy and paste to prevent the test failed), otherwise store the calculation in the `result` variable.

#### 6. Display the result contained in the `result` variable.

**Attention**: In this exercise, write your code in the part located below the line `def main()`. **Make sure to indent everything by one level** so that your code works correctly. We wrapped your code in what we call a function, to test your code we had to nest your code in this function.
