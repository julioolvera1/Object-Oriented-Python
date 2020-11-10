import numpy as np 

class RegularPolygon:
    ## Abstract class

    def __init__(self,colour,side_length):

        ## These are internal variables that should not be accessible outside of the class definition
        self._colour=colour
        self._side_length=side_length

    ## These are properties that set the internal variables

    @property
    def colour(self):
        return(self._colour)

    @property
    def side_length(self):
        return(self._side_length)

    @property
    def perimeter(self):
        return(self.number_sides*self.side_length)


### These two classes inherit from RegularPolygon

class Square(RegularPolygon):

    number_sides=4

    @property
    def area(self):
        area = self.side_length**2
        print(f'Square area: {area:.2f}')
        return(area)

class Triangle(RegularPolygon):

    number_sides = 3

    @property
    def area(self):
        area = np.sqrt(3) * self.side_length**2/4
        print(f'Triangle area: {area:.2f}')
        return(area)


square_1=Square('Red',3)
square_1.area

triangle_1=Triangle('Blue',4)
triangle_1.area
        
    
shapes=[]

shapes.append(square_1)
shapes.append(triangle_1)

for shape in shapes:

    print(f'Shape colour: {shape.colour}, shape area: {shape.area:.2f}')






