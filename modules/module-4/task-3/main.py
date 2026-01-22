user_input = None
smallestNumber = None
biggestNumber = None

while user_input != "":
	user_input = input("Enter number: ")

	if user_input == "":
		break

	if smallestNumber == None or user_input < smallestNumber:
		smallestNumber = user_input
	
	if biggestNumber == None or user_input > biggestNumber:
		biggestNumber = user_input

print(f"Biggest number: {biggestNumber}")
print(f"Smallest number: {smallestNumber}")