# -*- coding: utf-8 -*-


__author__ = 'FABIO RODRIGUES PEREIRA'
__email__ = 'faro@nmbu.no'


def bubble_sort(tuple_data):
    """
    :param tuple_data:
    - Write code for the bubble sort function;
    - The function shall not modify the list or tuple passed to it.
    :return:
    - A new list with the data in sorted order.
    """
    list_d = list(tuple_data)
    for pass_left in range(len(list_d) - 1, 0, -1):
        for i in range(pass_left):
            if list_d[i] > list_d[i + 1]:
                list_d[i], list_d[i + 1] = list_d[i + 1], list_d[i]
    return list_d


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert bubble_sort(empty_list) == empty_list == []


def test_single():
    """Test that the sorting function works for single-element list"""
    single_element_list = [1]
    assert bubble_sort(single_element_list) == single_element_list == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 2, 3] is not data == [3, 2, 1]


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1] is not sorted_data == [1, 2, 3]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == bubble_sort(sorted_data) is not data == [3,
                                                                   2, 1]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert bubble_sort(sorted_data[::-1]) == sorted_data is not data


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == data == bubble_sort(data)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = [
        [10, 1, 5],
        [1, 2, 5, 10, 6, 13, 9],
        [3, 1]
    ]
    sorted_data = [bubble_sort(i) for i in data]

    for a in range(len(data)):
        assert sorted_data[a] == bubble_sort(data[a]) != data
