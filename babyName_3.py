import random, string

letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')

vowels = 'aejouy'
consonants = 'bcdfghklmnpqrstvwxz'
letter = string.ascii_lowercase

def generator():
	if letter_input_1 == "v":
		letter_1 = random.choice(vowels)
	elif letter_input_1 == "c":
		letter_1 = random.choice(consonants)
	elif letter_input_1 == "l":
		letter_1 = random.choice(letter)
	else:
		letter_1 = letter_input_1 # To allow user to select a specific letter

	if letter_input_2 == "v":
		letter_2 = random.choice(vowels)
	elif letter_input_2 == "c":
		letter_2 = random.choice(consonants)
	elif letter_input_2 == "l":
		letter_2 = random.choice(letter)
	else:
		letter_2 = letter_input_2

	if letter_input_3 == "v":
		letter_3 = random.choice(vowels)
	elif letter_input_3 == "c":
		letter_3 = random.choice(consonants)
	elif letter_input_3 == "l":
		letter_3 = random.choice(letter)
	else:
		letter_3 = letter_input_3 

	if letter_input_4 == "v":
		letter_4 = random.choice(vowels)
	elif letter_input_4 == "c":
		letter_4 = random.choice(consonants)
	elif letter_input_4 == "l":
		letter_4 = random.choice(letter)
	else:
		letter_4 = letter_input_4 

	if letter_input_5 == "v":
		letter_5 = random.choice(vowels)
	elif letter_input_5 == "c":
		letter_5 = random.choice(consonants)
	elif letter_input_5 == "l":
		letter_5 = random.choice(letter)
	else:
		letter_5 = letter_input_5 

	name = letter_1 + letter_2 + letter_3 + letter_4 + letter_5
	return (name)

for babyNames in range(20):
	print(generator())