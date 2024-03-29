def main():
    # Get the user's input
    numbers = input("Enter a list of numbers separated by commas : ")

    # Separate the set of numbers and insert them into a list
    numbers = numbers.split(",")
    # Display the list of numbers
    print("List of numbers : ", numbers)

    # Calculate the sum of the numbers
    total_sum = 0
    for number in numbers:
        total_sum += int(number)
    print("Sum of numbers : ", total_sum)

    # Calculate the average using the sum of the numbers
    average = total_sum / len(numbers)
    print("Average of numbers :", average)

    # Find the number of integers greater than the average
    up_average_number = 0
    for number in numbers:
        if int(number) > average:
            up_average_number += 1
    print("Number of numbers greater than the average : ", up_average_number)

    # Find the number of even integers
    even_numbers = 0
    i = 0
    while i < len(numbers):
        if int(numbers[i]) % 2 == 0:
            even_numbers += 1
        i += 1
    print("Number of even numbers :", even_numbers)

# Do not modify the code below
if __name__ == "__main__":
    main()