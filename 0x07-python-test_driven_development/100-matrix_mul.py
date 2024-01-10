#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(el) == 0 for el in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(el) == 0 for el in m_b):
        raise ValueError("m_b can't be empty")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if any(
        not isinstance(el, int) and not isinstance(el, float)
        for el in [num for row in m_a for num in row]
    ):
        raise TypeError("m_a should contain only integers or floats")
    if any(
        not isinstance(el, int) and not isinstance(el, float)
        for el in [num for row in m_b for num in row]
    ):
        raise TypeError("m_b should contain only integers or floats")

    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]
    return result
