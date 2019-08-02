import random, string

def generator():
	letter_1 = random.choice(string.ascii_lowercase)
	letter_2 = random.choice(string.ascii_lowercase)
	letter_3 = random.choice(string.ascii_lowercase)
	letter_4 = random.choice(string.ascii_lowercase)
	letter_5 = random.choice(string.ascii_lowercase)
	name = letter_1 + letter_2 + letter_3 + letter_4 + letter_5
	return (name)

print(generator())

# Ask user for some input

letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')

#
vowels = 'aejouy'
consonants = 'bcdfghklmnpqrstvwxz'
letter = string.ascii_lowercase

if letter_input_1 == "v":
	letter_1 = random.choice(vowels)
elif letter_input_1 == "c":
	letter_1 = random.choice(consonants)
elif letter_input_1 == "l":
	letter_1 = random.choice(letter)
else:
	letter_1 = letter_input_1 # To allow user to select a specific letter
	 