#!/usr/bin/python3
"""Defines a class named Rectangle"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialises the rectangle with the given dimensions
        """
        self.width = width
        self.height = height
        type(self).number_of_instances = type(self).number_of_instances + 1

    @property
    def width(self):
        """
        Property getter to retrieve width size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter to set width size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property getter to retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter to set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Defines the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Defines the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints the rectange using the any given char
        """
        if self.__width == 0 or self.__height == 0:
            return f""
        else:
            string = ""
            for i in range(1, self.__height):
                string = string + str(self.print_symbol) * self.__width + '\n'
            else:
                string = string + str(self.print_symbol) * self.__width
            return string

    def __repr__(self):
        """
        Represents the repr() func to return
        a printable representation of the given object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deleting an instance
        """
        type(self).number_of_instances = type(self).number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns which rectangle is bigger
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that return a new instance where
        width and height are equal to size
        """
        return cls(size, size)
