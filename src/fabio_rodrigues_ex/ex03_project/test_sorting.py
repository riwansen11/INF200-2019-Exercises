# -*- coding: utf-8 -*-

__author__ = 'FABIO RODRIGUES PEREIRA'
__email__ = 'faro@nmbu.no'


def char_counts(textfilename):
    """
    1st. Opens the file with the given filename using encoding utf-8.
    2nd. Reads the entire file content into a single string.
    3rd. Counts how often each character code (0–255) occurs in the
    string.
    :return:
    The result as a list or tuple, where result[i] gives the number of
    occurrences of character code i.
    """
    with open(textfilename, 'r') as f:
        content = f.read()

    return [content.count(i) for i in content]


def test_empty():
    """Test that the sorting function works for empty list"""
    pass


def test_single():
    """Test that the sorting function works for single-element list"""
    pass


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
