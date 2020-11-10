## Circle class

import numpy as np

class Circle():


    n_circles_with_radius=0

    @staticmethod ## notice that no self is provided 
    def calculate_area(radius):
        area=np.pi*radius**2
        print(f'The area of the circle is: {area:.2f}')
        return area

    @classmethod ## notice that cls is provided
    def increment_n_circles_with_radius(cls):

        cls.n_circles_with_radius = cls.n_circles_with_radius + 1

        
    def set_radius(self,radius):

        self.radius=radius

        print('Radius for circle has been set')

        Circle.increment_n_circles_with_radius()

        print(f'Circles with radius set: {self.n_circles_with_radius}') ## notice that self is required


    def get_area(self):

        self.area=self.calculate_area(self.radius)
        
        return self.area


circle_1=Circle()
circle_1.set_radius(1)
circle_1.get_area()


circle_2=Circle()
circle_2.set_radius(2)
circle_2.get_area()

circle_3 = Circle()
circle_3.set_radius(3)
circle_3.get_area()








         

