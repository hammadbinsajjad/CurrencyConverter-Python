from conversions import *

def main():
    while True:
        print("Here are the choices for converions")

        # Enter your conversions here
        print("1. PKR to USD")
        print("2. SAR to PKR")
        print("3. PKR to Pound")

        choice = int(input("Enter your conversion choice: "))

        amount = float(input("Enter amount to convert: "))

        # Enter your conversion choices here
        if choice == 1:
            converted_amount = pkr_to_usd(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 2:
            converted_amount = sar_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")
            
        if choice == 3:
            converted_amount = pkr_to_pound(amount)
            print(f"The converted amount is {converted_amount}")

        cont = input("Do you want to continue? (Y)es or (N)o: ")

        if cont == "Y" or cont == "y":
            continue
        else:
            break


main()