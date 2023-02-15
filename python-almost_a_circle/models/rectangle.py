#!/usr/bin/python3
"""
A class named Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the instance of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle pattern with the '#' symbol in position
        according to x and y values
        """
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width, end='')
            print()

    def update(self, *args, **kwargs):
        """
        Args go through *args to assign an argument to the according attributes
        in the given order.
        If args is given in key, value pairs, arg goes through **kwargs
        """
        for key, value in kwargs.items():
            if key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            elif key == "id":
                self.id = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def __str__(self):
        """
        Overrides __str__ method to return the following statement
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
