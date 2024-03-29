import subprocess
import sys
import re

def run_main_file():
    python_cmd = "python" if sys.version_info.major == 2 else "python3"
    
    process = subprocess.Popen([python_cmd, "main.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output.decode()


def test_title():
    output = run_main_file()
    exepected_output = "HTML Extraction Exercise"
    assert exepected_output in output, "The title is not correctly extracted."

def test_h1():
    output = run_main_file()
    exepected_output = "Welcome to our website"
    assert exepected_output in output, "The h1 tag is not correctly extracted."

def test_product_10_euro():
    output = run_main_file()
    exepected_output = "10"
    assert exepected_output in output, "The product at 10 euros is not correctly extracted."

def test_product_20_euro():
    output = run_main_file()
    exepected_output = "20"
    assert exepected_output in output, "The product at 20 euros is not correctly extracted."

def test_product_30_euro():
    output = run_main_file()
    exepected_output = "30"
    assert exepected_output in output, "The product at 30 euros is not correctly extracted."

def test_description_1():
    output = run_main_file()
    exepected_output = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    assert exepected_output in output, "The description 1 is not correctly extracted."


def test_description_2():
    output = run_main_file()
    exepected_output = "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    assert exepected_output in output, "The description 2 is not correctly extracted."


def test_description_3():
    output = run_main_file()
    exepected_output = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    assert exepected_output in output, "The description 3 is not correctly extracted."

def test_conversion_dollar():
    output = run_main_file()
    assert "24.0" in output, "The product 1 is not correctly converted."
    assert "36.0" in output, "The product 2 is not correctly converted."
    assert "12.0" in output, "The product 3 is not correctly converted."