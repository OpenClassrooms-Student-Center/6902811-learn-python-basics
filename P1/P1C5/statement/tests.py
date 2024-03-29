import subprocess
import sys
import re

def run_main_file():
    python_cmd = "python" if sys.version_info.major == 2 else "python3"
    
    process = subprocess.Popen([python_cmd, "main.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output.decode()


def test_display_name():
    output = run_main_file()
    regex_pattern = r"[nN]ame\s?:\s?[A-Za-z]+"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Name: [Name in letters]' was not found in the console output."

def test_display_age():
    output = run_main_file()
    regex_pattern = r"[aA]ge\s?:\s?\d+"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Age: [Age in numbers]' was not found in the console output."

def test_display_height():
    output = run_main_file()
    regex_pattern = r"[hH]eight\s?:\s?\d+\.\d+"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Height: [Height in floating-point number]' was not found in the console output."

def test_display_is_student():
    output = run_main_file()
    regex_pattern = r"[iI]s\s?student\s?:\s?(True|False)"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Is student: [Is student in Boolean]' was not found in the console output."

def test_display_type_name():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[nN]ame\s?:\s?<class 'str'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Type name: [Type name]' was not found in the console output."

def test_display_type_age():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[aA]ge\s?:\s?<class 'int'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Type age: [Type age]' was not found in the console output."

def test_display_type_height():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[hH]eight\s?:\s?<class 'float'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Type height: [Type height]' was not found in the console output."

def test_display_type_is_student():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[iI]s\s?[sS]tudent\s?:\s?<class 'bool'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "The pattern 'Type is student: [Type is student]' was not found in the console output."

