airports = {
		"EFHK": "Helsinki-Vantaa Airport",
		"EFIV": "Ivalo Airport",
		"EFKU": "Kuopio Airport"
	}

def main():
	COMMAND_ADD = "ADD"
	COMMAND_SEARCH = "SEARCH"
	COMMAND_EXIT = "EXIT"

	isRunning = True

	while isRunning:
		print("Airports Database")
		print(f"{COMMAND_ADD} - Add new airport")
		print(f"{COMMAND_SEARCH} - Search for airports")
		print(f"{COMMAND_EXIT} - Exit the program")
		user_input = input("> ")

		if user_input.upper() == COMMAND_ADD:
			add()
		elif user_input.upper() == COMMAND_SEARCH:
			search()
		elif user_input.upper() == COMMAND_EXIT:
			isRunning = False

def add():
	code = input("Enter airport ICAO code: ").upper()
	name = input("Enter airport name: ")

	if (code == "" or name == ""):
		print("Couldn't add airport\nInput was invalid")
	else:
		airports.update({code: name})
		print(f"Airport {code} {name} added to database")


def search():
	user_code = input("Enter airplance ICAO code: ").upper()

	print(airports[user_code])

main()