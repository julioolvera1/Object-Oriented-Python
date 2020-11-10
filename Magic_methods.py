## Magic methods

class Square:

    def __init__(self, side_length):
        
        self.n_instances=0

        self.side_length = side_length

        print(f'Side length is: {side_length:.2f}')


    def calculate_area(self):

        area=self.side_length**2

        print(f'Area is: {area:.2f}')


    def class_counter(self):
        self.n_instances = self.n_instances+1



    
square_1=Square(3)
square_1.calculate_area()
