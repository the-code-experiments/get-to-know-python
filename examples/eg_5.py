def about(name, age, likes):
  return "Hello {}, my age is {} and I like {}".format(name, age, likes)

# def about(**kwargs):
#   for key, value in kwargs.items():
#     return "{}: {}".format(key, value)

data1 = {
  "name": "Ashwin",
  "age": 27,
  "likes": "Python"
}

data2 = {
  "likes": "Golang",
  "name": "Hegde",
  "age": 28
}

print(about(**data1))
print(about(**data2))