import main
from io import StringIO
import sys

def test_symbol_ok(mocker):
    mocker.patch('builtins.input', side_effect=['40', '10', '&'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "Error: the operation symbol must be '+', '-', '*', or '/'."
    assert expected_value in output

def test_sum(mocker):
    mocker.patch('builtins.input', side_effect=['5', '3', '+'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "8"
    assert expected_value in output

def test_substraction(mocker):
    mocker.patch('builtins.input', side_effect=['10', '5', '-'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "5"
    assert expected_value in output

def test_multiplication(mocker):
    mocker.patch('builtins.input', side_effect=['4', '7', '*'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "28"
    assert expected_value in output

def test_division(mocker):
    mocker.patch('builtins.input', side_effect=['40', '10', '/'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "4"
    assert expected_value in output

def test_zero_division(mocker):
    mocker.patch('builtins.input', side_effect=['40', '0', '/'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "Error: division by zero is not allowed."
    assert expected_value in output