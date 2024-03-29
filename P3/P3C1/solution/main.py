# In the main file, we can import functions from operations.py 
# using the import statement, and then use them to perform operations.
import operations


def main():
    # Call the function sum()
    sum_result = operations.sum(3, 5)
    print("Result of the sum :", sum_result)
    # Call the function product()
    product_result = operations.product(8, 2)
    print("Result of the product :", product_result)


if __name__ == "__main__":
    main()