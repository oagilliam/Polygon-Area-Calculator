


class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

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
    
    def get_amount_inside(self, width2, height2):
        if width2 == height2:
            self.square = width2**2
            amount_square = (self.width *self.height) / self.square
