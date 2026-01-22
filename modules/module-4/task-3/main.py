user_numbers = []
user_input = None

while user_input != "":
	user_input = input("Enter number: ")

	if user_input == "":
		break

	user_numbers.append(user_input)

print(sorted(user_numbers))