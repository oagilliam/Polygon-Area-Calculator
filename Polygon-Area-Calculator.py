


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self):
        return self.width
    
    def set_height(self):
        return self.height
    
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
            tooBig = 'Too big for picture'
            return tooBig
        else:
            for row in range(self.height):
                print("*", end="")
                for column in range(self.width-1):
                    print('*', end="")
                print("\n")
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / self.get_area())
        
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self):
        return self.width
    
    def set_width(self):
        return self.width
    
    def set_height(self):
        return self.height

r = Rectangle(50,26)
#sqr = Square(4)
#print(r.set_width())
#print(r.set_height())
#print(r.get_area())
#print(r.get_perimeter())
#print(r.get_diagonal())
#print(r.get_picture())