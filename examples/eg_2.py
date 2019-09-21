subjects = {"English": 10, "Spanish": 25, "Hindi": 5, "Gujarati": 15, "Kannada": 35}
print("Here are the list of subjects")
print(subjects)

choosenSubject = input("What subject would you like to choose? ").strip().capitalize()

if choosenSubject in subjects:
  print("Subject do exist")
  
  changeSubjectCode = input("Would you like to changes the " + choosenSubject + " subject's code? (y/n) ").lower()
  if changeSubjectCode == 'y':
    newSubjectCode = input("Please specific the new subject code for " + choosenSubject + " subject: ")
    subjects[choosenSubject] = int(newSubjectCode)
else:
  print("Subject do not exist")

  shouldAddNewSubject = input("Would you like to add " + choosenSubject + " as new subject? (y/n) ").lower()

  if shouldAddNewSubject == 'y':
    newSubjectCode = input("What subject code would you like to give for subject " + choosenSubject + "? ")
    subjects[choosenSubject] = int(newSubjectCode)

print("Here are the updated list of subjects")
print(subjects)