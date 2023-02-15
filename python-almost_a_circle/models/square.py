"""
A class named Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that inherits methods and attributes from Rectangle
    and defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates a new object
        """
        super().__init__(size, size, x, y, id)
        self.size = size
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
