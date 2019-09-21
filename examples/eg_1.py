languages = ["English", "Spanish", "Hindi", "Gujarati", "Kannada"]

print("Hello There! \nI can speak either of these language")
print(languages)

name = input("\nWhat is your name? ")
print("Hello {}".format(name))

currentLanguage = input("What language do you speak? ").strip().capitalize()
if currentLanguage in languages:
  print("I do speak, " + currentLanguage)

  removeLanguage = input("Should I unlearn the " + currentLanguage + " language? (y/n) ").strip().lower()
  if removeLanguage == 'y':
    languages.remove(currentLanguage)
    print("I unlearnt " + currentLanguage + " language. Now I known either of these languages")
    print(languages)
else:
  print("I don't speak " + currentLanguage + ", try another language!")

  addLanguage = input("Should I learn the " + currentLanguage + " language? (y/n) ").strip().lower()
  if addLanguage == 'y':
    languages.append(currentLanguage)
    print("I learnt " + currentLanguage + " language.")
    print(languages)
