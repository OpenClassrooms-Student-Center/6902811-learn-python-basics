def main():
    left_number = input("Enter an integer number : ")
    right_number = input("Enter an integer number : ")
    operation = input("Enter the desired operation ['+', '-', '*', or '/'] : ")

    result = 0

    # Check if both numbers are valid using the isinstance() function (either an integer or a float)
    if not left_number.isnumeric() or not right_number.isnumeric():
        print("Error: both numbers must be integers")
    else:
        left_number = int(left_number)
        right_number = int(right_number)
        
        match operation:
            case "+":
                result = left_number + right_number
            case "-":
                result = left_number - right_number
            case "*":
                result = left_number * right_number
            case "/":
                # Check if the variable right_number is not zero for division.
                if right_number == 0:
                    print("Error: division by zero is not allowed.")
                else:
                    result = left_number / right_number
            # If we are in the default case, it means the symbol is incorrect.
            case _:
                print("Error: the operation symbol must be '+', '-', '*', or '/'.")

        # print the result
        print(f"The result of the operation is: {result}")

if __name__ == "__main__":
    main()