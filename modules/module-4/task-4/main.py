import random

minNumber = 1
maxNumber = 10

generatedNumber = random.randint(minNumber, maxNumber)
userGuess = None

while generatedNumber != userGuess:
	userGuess = int(input(f"Guess the number from {minNumber}-{maxNumber}:"))

	if userGuess == generatedNumber:
		break

	if userGuess > generatedNumber:
		print("Your guess is too large")
	elif userGuess < generatedNumber:
		print("Your guess was too small")

print(f"Correct! The number was {generatedNumber}")