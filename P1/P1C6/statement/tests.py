from main import fruits

def test_kiwi_in_list():
    expected_value = "kiwi"
    assert expected_value in fruits, "Kiwi is not in the list."

def test_orange_removed():
    expected_value = "orange"
    assert expected_value not in fruits, "Orange is still in the list."

def test_ananas_replace_banane():
    replaced_value = "pineapple"
    removed_value = "banana"
    assert replaced_value in fruits, "Pineapple has not been added to the list."
    assert removed_value not in fruits; "Banana has not been replaced in the list."

def test_list_sorted():
    not_expected_value = ['apple', 'pineapple', 'kiwi']
    expected_value = ['apple', 'kiwi', 'pineapple']
    assert not_expected_value != fruits
    assert expected_value == fruits, "The list is not sorted"