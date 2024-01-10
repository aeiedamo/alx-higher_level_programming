#!/usr/bin/python3
"""Lazy matrix multiplication"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices by using the module NumPy"""
    return numpy.dot(m_a, m_b)
