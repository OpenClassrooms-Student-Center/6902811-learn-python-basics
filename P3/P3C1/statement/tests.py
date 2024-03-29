from io import StringIO
import sys
from main import main
from operations import product, sum

def test_main():
    output = StringIO()
    sys.stdout = output
    main()
    output_value = output.getvalue().strip()
    sys.stdout = sys.__stdout__
    assert '8' in output_value, "The functions are not correctly called, or you are not displaying the results."
    assert '16'in output_value, "The functions are not correctly called, or you are not displaying the results."

def test_product():
  assert product(10, 5) == 50, "The function product is not correctly defined."

def test_sum():
  assert sum(10, 5) == 15, "The function sum is not correctly defined."