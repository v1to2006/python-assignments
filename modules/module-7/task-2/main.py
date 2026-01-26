def fill_names():
	names = []
	input_message = "Enter new name: "

	user_input = input(input_message)

	while user_input != "":
		if item_exists(names, user_input):
			print("Name already exists")
		else:
			names.append(user_input)
			print("New name added")

		user_input = input(input_message)
	
	return names

def item_exists(list, item) -> bool:
	for i in list:
		if i == item:
			return True
	
	return False

def print_list(list, title):
	print(f"{title}:\n")

	for i in list:
		print(f"{i}")

def main():
	names = fill_names()

	print_list(names, "Names")

main()