class Plant:
  """A class used by a plant nursery to track what plants they have in inventory 
  and how many they have of each plant.

  >>> milkweed = Plant("Narrow-leaf milkweed", "Asclepias fascicularis")
  >>> milkweed.common_name
  'Narrow-leaf milkweed'
  >>> milkweed.latin_name
  'Asclepias fascicularis'
  >>> milkweed.inventory
  0
  >>> milkweed.update_inventory(2)
  >>> milkweed.inventory
  2
  >>> milkweed.update_inventory(3)
  >>> milkweed.inventory
  5
  """

  def __init__(self, common_name, latin_name):
    self.common_name = common_name
    self.latin_name = latin_name
    self.inventory = 0
    
  def update_inventory(self, amount):
    self.inventory += amount
    
    
milkweed = Plant("Narrow-leaf milkweed", "Asclepias fascicularis")

print(milkweed.inventory)

milkweed.update_inventory(2)
print(milkweed.inventory)


class Clothing:
  """A class that represents pieces of clothing in a closet,
  tracking the color, category, and clean/dirty state.

  >>> blue_shirt = Clothing("shirt", "blue")
  >>> blue_shirt.category
  'shirt'
  >>> blue_shirt.color
  'blue'
  >>> blue_shirt.is_clean
  True
  >>> blue_shirt.wear()
  >>> blue_shirt.is_clean
  False
  >>> blue_shirt.clean()
  >>> blue_shirt.is_clean
  True
  """

  def __init__(self, category, color):
      self.category = category
      self.color = color
      self.is_clean = True
  
  def wear(self):
      self.is_clean = False

  def clean(self):
      self.is_clean = True



item_1 = Clothing("pantalone", "grey")

item_1.wear()
print(item_1.is_clean)

item_1.clean()
print(item_1.is_clean)