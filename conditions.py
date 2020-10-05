temp = 0
tempMax = 999
answer = ""

while answer != "N":
    temp = int(input("Please enter the current temperature: "))
    
    if temp == tempMax:
        break
    elif temp > 90:
        print("\nYou will have to wear shorts.")
    elif temp > 70:
        print("\nShort sleeves are fine to wear.")
    elif temp > 50:
        print("\nWear a jacket, please.")
    elif temp > 32:
        print("\nPlease wear a heavy coat.")
    else:
        print("\nIt is too cold. Stay inside!")

    answer = str(input("\nWould you like to enter another temperature? (Enter Y/N) "))
    if answer == "Y":
        print()
        continue
    else:
        continue
else:
    print()
    print("The program has ended.")
    print()
