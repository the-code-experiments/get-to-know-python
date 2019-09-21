class Coin:

  def __init__(self, rare=False, clean=True, **kwargs):

    for key, value in kwargs.items():
      setattr(self, key, value)

    self.is_rare = rare
    self.is_clean = clean

    if self.is_rare:
      self.value = self.original_value * 1.25
    else:
      self.value = self.original_value
    
    if self.is_clean:
      self.color = self.clean_color
    else:
      self.color = self.rusty_color

  def rust(self):
    self.color = self.rusty_color

  def clean(self):
    self.color = self.clean_color

  def __del__(self):
    print("Coin spent!")


class Pound(Coin):

  def __init__(self):
    data = {
      "original_value": 1.00,
      "clean_color": "Gold",
      "rusty_color": "Greenish",
      "edges": 1,
      "diameter": 22.5,
      "thinkness": 3.15,
      "mass": 9.5
    }
    
    super().__init__(**data)

class Doller(Coin):

  def __init__(self):
    data = {
      "original_value": 2.00,
      "clean_color": "Silver",
      "rusty_color": "Brownish",
      "edges": 1,
      "diameter": 20.5,
      "thinkness": 2.15,
      "mass": 6.5
    }
    
    super().__init__(**data)
  
  # Polymorphism
  def rust(self):
    self.color = self.clean_color

coin1 = Pound()
print(coin1.color)
coin1.rust()
print(coin1.color)

coin2 = Doller()
print(coin2.color)
coin2.rust()
print(coin2.color)
