import main
from io import StringIO
import sys

def test_display_list(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "['1', '3', '5', '6']"
    assert expected_value in output

def test_sum(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "15"
    assert expected_value in output

def test_average(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "3.75"
    assert expected_value in output

def test_average_up(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "2"
    assert expected_value in output

def test_even_number(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "1"
    assert expected_value in output