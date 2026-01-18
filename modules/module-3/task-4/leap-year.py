inputYear = int(input("Enter a year: "))

if ((inputYear % 4 == 0) and (inputYear % 100 != 0)) or ((inputYear % 400 == 0)):
    print(f"{inputYear} IS a leap year.")
else:
    print(f"{inputYear} IS NOT a leap year.")