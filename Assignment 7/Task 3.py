#!/usr/bin/env python3

class Matrix:

    def __init__(self, matrix):
        assert type(matrix) == list, "matrix should be entered as a nested list"
        assert len(matrix) > 0, "matrix initialization must not contain empty lists"
        for row in matrix:
            assert type(row) == list, "matrix should be entered as a nested list"
            assert len(row) > 0, "matrix initialization must not contain empty lists"
            for el in row:
                assert type(el) == float or type(el) == int, "matrix should be two dimensional and contain either integers or floats."
        col_len = len(matrix[0])
        for r in matrix[1:]:
            assert col_len == len(r), "not all columns are of the same length"
        self.__matrix = matrix

    def get_dimensions(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        assert self.get_dimensions() == other.get_dimensions()
        new = []
        for i, r in enumerate(self.__matrix):
            newr = []
            for j, el in enumerate(r):
                newr.append(el + other.__matrix[i][j])
            new.append(newr)
        return Matrix(new)


    def __mul__(self, other):
        assert self.get_dimensions()[1] == other.get_dimensions()[0], "assert text"
        new = []
        for i in range(len(self.__matrix)):
            newr = []
            for j in range(len(other.__matrix[0])):
                el_sum = 0
                for run_idx in range(len(self.__matrix[0])):
                    el_sum += self.__matrix[i][run_idx] * other.__matrix[run_idx][j]
                newr.append(el_sum)
            new.append(newr)
        return Matrix(new)


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Matrix({self.__matrix.__str__()})"

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))

