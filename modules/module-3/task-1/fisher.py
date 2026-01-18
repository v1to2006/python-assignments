fishSize = int(input("What size fish is? (cm): "))

minFishSize = 37

if fishSize < minFishSize:
    print("The fish is too small, throw it back.")
    print(f"Fish misses the minimum size by {minFishSize - fishSize} cm.")
else:
    print("The fish is big enough, keep it.")