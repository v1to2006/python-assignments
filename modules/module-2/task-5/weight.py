leiviskat = input("Anna leiviskat: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

naulaMultiplier = 20
luodiMultiplier = 32
gramMultiplier = 13.3

totalNaulat = float(leiviskat) * naulaMultiplier + float(naulat)
totalLuodit = float(totalNaulat) * luodiMultiplier + float(luodit)
totalGrammat = float(totalLuodit) * gramMultiplier

displayedKilograms = int(totalGrammat / 1000)
displayedGrams = round(totalGrammat % 1000, 2)

print(f"Massa nykymittojen mukaan: {displayedKilograms} kilogrammaa ja {displayedGrams} grammaa.")