import pytest
from data_structures.linked_list import LinkedList, TargetError


# @pytest.mark.skip("TODO")
def test_kth_from_end_zero():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_one():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_two():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_out_of_range():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


# @pytest.mark.skip("TODO")
def test_kth_from_end_under_range():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


# @pytest.mark.skip("TODO")
def test_kth_from_end_size_one():
    linked_list = LinkedList()
    linked_list.insert("apples")
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected

def test_kth_from_end_size_two():
    linked_list = LinkedList()
    linked_list.insert("apples")
    linked_list.insert("bananas")
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected

def test_kth_from_end_size_two_2():
    linked_list = LinkedList()
    linked_list.insert("apples")
    linked_list.insert("bananas")
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


def test_target_error():
  try:
    raise TargetError("This specific error")
  except TargetError as e:
    print(f"Caught TargetErrorL {e}")

# class TargetError
# cd into  python->tests->code_challenges
# pytest test_linked_list_kth.py
