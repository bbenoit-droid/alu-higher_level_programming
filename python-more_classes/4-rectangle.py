#!/usr/bin/python3
"""
Module defining a Rectangle class with capabilities to calculate area,
perimeter, and generate string representations of the rectangle.
"""


class Rectangle:
    """A class to represent a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """
        Generate a string representation of the rectangle using '#'.

        Returns:
            str: The rectangle visualized with '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append('#' * self.__width)
        return "\n".join(rect_lines)

    def __str__(self):
        """
        Return the informal string representation of the rectangle.

        Returns:
            str: The rectangle visualized with '#' characters.
        """
        return self._draw_rectangle()

    def __repr__(self):
        """
        Return the official string representation of the rectangle.

        Returns:
            str: A string that can be used to recreate this rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
