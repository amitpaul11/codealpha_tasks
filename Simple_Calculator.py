print("===== PYTHON CALCULATOR =====")

print("\n CHOOSE OPERATION: ")
print("1: ADDITION (+):")
print("2: SUBTRACTION (-):")
print("3: MULTIPLICATION (*):")
print("4: DIVISION (/):")
print("5: REMAINDER (%):")
print("6: POWER (^):")

CHOICE = input("Enter Choice (1-6):")

NUM_1 = float(input("Enter First Number:"))
NUM_2 = float(input("Enter Second Number:"))

if CHOICE == "1":
    print("RESULT = ",NUM_1 + NUM_2)
elif CHOICE == "2":
    print("RESULT = ",NUM_1 - NUM_2)
elif CHOICE == "3":
    print("RESULT = ",NUM_1 * NUM_2)
elif CHOICE == "4":
    if NUM_2 != 0:
        print("RESULT = ",NUM_1 / NUM_2)
    else:
        print("CANNOT DIVIDED BY ZERO.") 
elif CHOICE == "5":
    if NUM_2 != 0:
        print("RESULT = ",NUM_1 % NUM_2)
    else:
        print("CANNOT DIVIDED BY ZERO.")  
elif CHOICE == "6":
    print("RESULT = ",NUM_1 ** NUM_2)              
else:         
    print("<<< INVALID CHOICE >>>") 