from conversions import *

def main():
    while True:
        print("Here are the choices for converions")

        # Enter your conversions here
        print(" 1. PKR to USD")
        print(" 2. SAR to PKR")
        print(" 3. PKR to GBP")
        print(" 4. PKR to AED")
        print(" 5. PKR to RUR")
        print(" 6. PKR to CNY")
        print(" 7. CNY to PKR")
        print(" 8. PKR to BHD")
        print(" 9. BHD to PKR")
        print("10. PKR to INR")
        print("11. INR to PKR")
        print("12. BDT to PKR")
        print("13. PKR to BDT")
        print("14. DKK to PKR")
        print("15. PKR to DKK")
        print("16. EUR to PKR")
        print("17. PKR to EUR")
        print("18. WON to PKR")
        print("19. PKR to WON")
        print("20. LIRA to PKR")
        print("21. PKR to LIRA")
        print("22. PKR to RIAL")
        print("23. RIAL to PKR")


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

        if choice == 4:
            converted_amount = pkr_to_aed(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 5:
            converted_amount = pkr_to_russianruble(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 6:
            converted_amount = pkr_to_yuan(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 7:
            converted_amount = yuan_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 8:
            converted_amount = pkr_to_bahrain_dinar(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 9:
            converted_amount = bahrain_dinar_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 10:
            converted_amount = pkr_to_inr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 11:
            converted_amount = inr_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 12:
            converted_amount = takka_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 13:
            converted_amount = pkr_to_takka(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 14:
            converted_amount = dkk_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 15:
            converted_amount = pkr_to_dkk(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 16:
            converted_amount = euro_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 17:
            converted_amount = pkr_to_euro(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 18:
            converted_amount = won_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 19:
            converted_amount = pkr_to_won(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 20:
            converted_amount = lira_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 21:
            converted_amount = pkr_to_lira(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 22:
            converted_amount = pkr_to_rial(amount)
            print(f"The converted amount is {converted_amount}")

        if choice == 23:
            converted_amount = rial_to_pkr(amount)
            print(f"The converted amount is {converted_amount}")

        cont = input("Do you want to continue? (Y)es or (N)o: ")

        if cont == "Y" or cont == "y":
            continue
        else:
            break


main()