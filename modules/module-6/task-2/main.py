import random

def throw_dice(max_number) -> int:
	min_number = 1

	return random.randint(min_number, max_number)

def main():
	currentDiceNumber = None
	targetNumber = int(input("Enter max number: "))

	while currentDiceNumber != targetNumber:
		currentDiceNumber = throw_dice(targetNumber)

		print(currentDiceNumber)

main()