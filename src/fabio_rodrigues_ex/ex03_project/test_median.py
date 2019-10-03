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
