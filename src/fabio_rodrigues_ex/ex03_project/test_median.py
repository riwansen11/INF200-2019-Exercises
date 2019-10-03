# -*- coding: utf-8 -*-
import pytest

__author__ = 'FABIO RODRIGUES PEREIRA'
__email__ = 'faro@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n // 2] if n % 2 == 1

            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_one_element_list():
    """A test that the median function returns the correct value for
    a one-element list
    """
    one_element_list = [8]
    assert median(one_element_list) == 8


@pytest.mark.parametrize('odd_list, even_list, list_ordered, '
                         'list_rev_ordered, list_unordered, result',
                         [
                             [
                                 (1, 3, 5),
                                 (1, 2, 4, 5),
                                 (1, 2, 3, 4, 5),
                                 (5, 4, 3, 2, 1),
                                 (2, 1, 5, 4, 3),
                                 3
                             ]
                         ]
                         )
def test_several(odd_list, even_list, list_ordered,
                 list_rev_ordered, list_unordered, result):
    """Several tests that check that the correct median is returned for
    - Lists with odd numbers of elements
    - Lists with even numbers of elements
    - Ordered list,
    - List with reverse-ordered
    - List with unordered elements
    """
    assert median(odd_list) == result
    assert median(even_list) == result
    assert median(list_ordered) == result
    assert median(list_rev_ordered) == result
    assert median(list_unordered) == result
