import math

class Shape:
    def area(self):
        """
        Raises NotImplementedError to indicate that derived classes need to override this method.
        
        Raises:
            NotImplementedError: To prompt overriding in derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance with length and width.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        
        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle instance with radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        
        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
