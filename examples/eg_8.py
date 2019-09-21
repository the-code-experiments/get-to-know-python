# def div42by(divBy):
#   return 42 / divBy

def div42by(divBy):
  try:
    return 42 / divBy
  # except ZeroDivisionError:
  #   return "Error: you tried to divid by zero!"
  except:
    return "Error: you tried to divid by zero!"

print(div42by(2))
print(div42by(0))
print(div42by(3))