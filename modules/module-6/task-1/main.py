import random

def throw_dice() -> int:
	min = 1
	max = 6

	return random.randint(min, max)

def main():
	currentDiceNumber = None
	targetNumber = 6

	while currentDiceNumber != targetNumber:
		currentDiceNumber = throw_dice()

		print(currentDiceNumber)

main()