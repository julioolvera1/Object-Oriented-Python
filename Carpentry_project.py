# Define a product class to define values common to all products
class Product:
  # Define class variables for the costs of components
  # It's best to do this here as it means it can be updated in a single place if values change
  cost_per_nail = 1
  cost_per_wood = 5

  # Define the property which returns the cost of materials
  @property
  def cost(self):
    return(self.n_nails * self.cost_per_nail + self.wood * self.cost_per_wood)


# Define a class to represent a desk
class Desk(Product):
  # Set the length and width of the desk
  def __init__(self, length, width):
    self.length = length
    self.width = width

  # A property to return the number of nails
  @property
  def n_nails(self):
    return(4)

  # A property to return the amount of wood required
  @property
  def wood(self):
    return(2 * self.length * self.width + 4)

# Define a class to represent a fence
class Fence(Product):
  # Set the length of the fence
  def __init__(self, length):
    self.length = length

  # A property to return the number of nails
  @property
  def n_nails(self):
    return(self.length * 2)

  # A property to return the amount of wood required
  @property
  def wood(self):
    return(self.length * 4)

# Define a class to represent a chair
class Chair(Product):
  # No constructor is needed as no values are set
  # The number of nails and amount of wood required can be set as class variables
  # These values can still be read from instances of Chair
  n_nails = 8
  wood = 4

# Write the function to calculate the cost of the products
def cost(products):
  # Accunmulate the total cost in "cost"
  cost = 0
  # Loop over the products
  for product in products:
    # Add the cost of each product to "cost"
    cost = cost + product.cost
  
  # Once all the products have been looped over, return "cost"
  return(cost)

# Create the array of products
products = []
products.append(Desk(2,1))
products.append(Fence(10))
products.append(Fence(12))
for i in range(3):
  products.append(Chair())
products.append(Desk(3,2))

# Find the cost of the products
print(cost(products))