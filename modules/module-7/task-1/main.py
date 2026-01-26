months = {
	1: "talvi",
	2: "talvi",
	3: "kevat",
	4: "kevat",
	5: "kevat",
	6: "kesa",
	7: "kesa",
	8: "kesa",
	9: "syksy",
	10: "syksy",
	11: "syksy",
	12: "talvi",
}

def main():
	month_number = int(input("Enter month number (1-12): "))

	if (month_number > 0 and month_number <= len(months)):
		print(months[month_number])
	else:
		print("Invalid input...")

main()