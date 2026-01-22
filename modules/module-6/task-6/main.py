import math

def convert_to_unit_price(diameter, price):
	radius = (diameter / 2) / 100
	area = math.pi * radius ** 2

	return price / area

def main():
	pizza_unit_price_1 = convert_to_unit_price(float(input("Enter pizza 1 diameter: ")), float(input("Enter pizza 1 price: ")))
	pizza_unit_price_2 = convert_to_unit_price(float(input("Enter pizza 2 diameter: ")), float(input("Enter pizza 2 price: ")))

	print(f"1st pizza unit price: {pizza_unit_price_1}")
	print(f"2nd pizza unit price: {pizza_unit_price_2}")

	if (pizza_unit_price_1 < pizza_unit_price_2):
		print(f"Pizza 1: better value")
	elif (pizza_unit_price_2 < pizza_unit_price_1):
		print(f"Pizza 2: better value")
	else:
		print(f"Both pizza values are equal")

main()