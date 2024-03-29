from main import fruits, couleur_banane

def test_fruits_dictionary():
  assert isinstance(fruits, dict), "fruits is not a dictionary"

def test_banana_removed():
    element_to_check = "banana"
    assert element_to_check not in fruits, "The key `banana was not properly deleted."

def test_apple_value():
    expected_value = "green"
    assert fruits["apple"] == expected_value, "The key `apple` was not properly modified to the value `green`."

def test_kiwi_in_dictionary():
    element_to_check = "kiwi"
    expected_value = "green"
    assert element_to_check in fruits, "The key `kiwi` is not in the dictionary."
    assert fruits[element_to_check] == expected_value, "The key `kiwi` does not have the correct value: `green`."

def test_final_dictionary_content():
    assert "apple" in fruits
    assert "kiwi" in fruits
    assert "orange" in fruits
    assert fruits["apple"] == "green"
    assert fruits["kiwi"] == "green"
    assert fruits["orange"] == "orange"

def test_banana_color_extract():
    expected_value = "yellow"
    assert couleur_banane == expected_value, "The color of the banana was not extracted: yellow"