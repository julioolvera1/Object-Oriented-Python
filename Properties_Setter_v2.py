class Square:
  def __init__(self, side_length):
    # The constructor will now access the property setter "side_length"
    self.side_length = side_length

  @property
  def side_length(self):
    return(self._side_length)

  @side_length.setter
  def side_length(self, value):
    if value < 0:
      raise ValueError("A square must have a side length of zero or greater")
    self._side_length = value
    
  def area(self):
    area = self._side_length ** 2
    return(area)

my_square = Square(2)
print(my_square.area)
# The side_length property setter will be called
# A value of 3 will be given to "value" when this function is called
my_square.side_length = 3
print(my_square.side_length)
print(my_square.area())
my_square.side_length = -1