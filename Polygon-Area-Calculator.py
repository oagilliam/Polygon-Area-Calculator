# In this project you will use object oriented programming to create a
# Rectangle class and a Square class. The Square class should be a subclass of
# Rectangle and inherit methods and attributes.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter 
    
    def get_diagonal(self):
        diagonal = ((self.height)**2 + (self.width)**2)**.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return "Too big for picture."
        
        shapeString = ""
        for row in range(self.height):
          shapeString += "*" * self.width + "\n"
        return shapeString
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
      
class Square(Rectangle):
    def __init__(self, side):
      super().__init__(side, side)

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)