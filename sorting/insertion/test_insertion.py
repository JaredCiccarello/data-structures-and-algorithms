import pytest
from insertion.insertion_sort import insert, insertion_sort

# @pytest.mark.skip("TODO")
def test_exists():
    sorted_array = [4, 8, 15, 16]  # Example sorted array
    value = 23  # Example value to insert
    result = insert(sorted_array, value)
    assert result is None

# @pytest.mark.skip("TODO")
def test_sort_positive_integers():
    input_array = [8, 4, 23, 42, 16, 15]
    expected_output = [4, 8, 15, 16, 23, 42]
    assert insertion_sort(input_array) == expected_output

# @pytest.mark.skip("TODO")
def test_sort_negative_integers():
    input_array = [-10, -5, -8, -3, -1, -7]
    expected_output = [-10, -8, -7, -5, -3, -1]
    assert insertion_sort(input_array) == expected_output

# @pytest.mark.skip("TODO")
def test_sort_duplicate_elements():
    input_array = [5, 2, 7, 5, 3, 2]
    expected_output = [2, 2, 3, 5, 5, 7]
    assert insertion_sort(input_array) == expected_output

# @pytest.mark.skip("TODO")
def test_sort_single_element():
    input_array = [42]
    expected_output = [42]
    assert insertion_sort(input_array) == expected_output
