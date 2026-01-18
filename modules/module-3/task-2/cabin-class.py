CLASS_LUX_ID = "LUX"
CLASS_A_ID = "A"
CLASS_B_ID = "B"
CLASS_C_ID = "C"

CLASS_LUX_ID_DESCRIPTION = f"{CLASS_LUX_ID} on parvekkeellinen hytti yläkannella."
CLASS_A_ID_DESCRIPTION = f"{CLASS_A_ID} on ikkunallinen hytti autokannen yläpuolella."
CLASS_B_ID_DESCRIPTION = f"{CLASS_B_ID} on ikkunaton hytti autokannen yläpuolella."
CLASS_C_ID_DESCRIPTION = f"{CLASS_C_ID} on ikkunaton hytti autokannen alapuolella."

selectedClass = input(f"Enter cabin class ({CLASS_LUX_ID}, {CLASS_A_ID}, {CLASS_B_ID}, {CLASS_C_ID}): ")

if selectedClass.upper() == CLASS_LUX_ID:
    print(f"{CLASS_LUX_ID_DESCRIPTION}")
elif selectedClass.upper() == CLASS_A_ID:
    print(f"{CLASS_A_ID_DESCRIPTION}")
elif selectedClass.upper() == CLASS_B_ID:
    print(f"{CLASS_B_ID_DESCRIPTION}")
elif selectedClass.upper() == CLASS_C_ID:
    print(f"{CLASS_C_ID_DESCRIPTION}")
else:
    print("Invalid cabin class")