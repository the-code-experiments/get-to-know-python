#!/usr/bin/python3

class Profile:
	def __init__(self, name = "Unknown", age = 18):
		self.name = name
		self.age = age

	def whatName(self):
		return self.name

	def whatAge(self):
		return self.age

def main():
	myProfile = Profile()
	print(myProfile.whatName(), myProfile.whatAge())

	github = Profile('Ashwin Hegde', age = 26)
	print(github.whatName(), github.whatAge())


if __name__ == "__main__": main()