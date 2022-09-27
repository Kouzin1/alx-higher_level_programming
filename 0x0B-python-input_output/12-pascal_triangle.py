#!/usr/bin/python3
""" Defines a pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integer representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for 1 in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
