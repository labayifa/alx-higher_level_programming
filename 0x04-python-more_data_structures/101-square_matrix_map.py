#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    Matrix square return
    :param matrix:
    :return:
    """
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))