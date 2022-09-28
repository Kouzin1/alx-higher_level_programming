#!/usr/bin/python3
# -*- codinfg: utf-8 -*-
"""
Created on Wed Sep 28 18:45:45 2022

@author: Akinwunmi Samuel
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """
        Init function for Square

        Attributes:
            size (int): The szie of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str function to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
