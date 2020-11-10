## Properties
class Square:

    def __init__(self,side_length):
        self.side_length=side_length

    @property #rather than accessing it as a method, it works as an instance variable
    def area(self):
        area=self.side_length**2
        return area  ## this one is needed, otherwise the return would be None


square_1=Square(3)

print(square_1.area)
