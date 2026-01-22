def get_even_numbers(numbers):
	new_numbers = []

	for i in numbers:
		if (i % 2 == 0):
			new_numbers.append(i)
	
	return new_numbers

def main():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	print(f"List: {numbers}")
	print(f"New list: {get_even_numbers(numbers)}")

main()