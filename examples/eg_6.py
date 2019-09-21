class Pound:

  # Constructor method
  def __init__(self, rare=False):
    self.rare = rare

    if self.rare:
      self.value = 1.25
    else:
      self.value = 1.00

    self.color = "Gold"
    self.edges = 1 # shape
    self.diameter = 22.5 # mm
    self.thickness = 3.15 # mm
    self.heads = True

  def rust(self):
    self.color = "Greenish"

  def clean(self):
    self.color = "Gold"

  # Distructor method
  def __del__(self):
    print("Coin spent!")


coin1 = Pound()
print(type(coin1))
print(coin1.color)

coin1.color = "Yellow"
print(coin1.color)

coin2 = Pound()
print(coin2.color)

coin3 = Pound(rare=True)
print(coin3.rare)
print(coin3.value)

coin3.rust()
print(coin3.color)
coin3.clean()
print(coin3.color)

# del coin1