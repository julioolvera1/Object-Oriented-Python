## Properties
class Square:

    def __init__(self,side_length):
        self._side_length=side_length 
        ## the underscore represents that this is an internal variable that should not be accessible outside of the class definition

        
    @property
    def side_length(self):
        return (self._side_length)

    @side_length.setter
    def side_length(self,value):
        if value<0:
            raise ValueError(f'Length must be greater than zero, increase {value}')

        self._side_length=value


    @property #rather than accessing it as a method, it works as an instance variable
    def area(self):
        area=self._side_length**2
        print(f'Area of square is: {area:.2f}')
        return area  ## this one is needed, otherwise the return would be None


square_1=Square(3)
print(square_1.area)

square_1.side_length=5
print(square_1.area)

square_1.side_length=-3
print(square_1.area)
