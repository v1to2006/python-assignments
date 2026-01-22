user_number = int(input("Enter number: "))
isAlkuLuku = True

for i in range(user_number):
	if (i == 0 or i == 1 or i == user_number):
		continue

	if (user_number % i == 0):
		isAlkuLuku = False
		break

if isAlkuLuku:
	print(f"{user_number} on alkuluku")
else:
	print(f"{user_number} ei ole alkuluku ")