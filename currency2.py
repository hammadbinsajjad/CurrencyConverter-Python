def pkr_to_bahrain_dinar(amount):
    return 0.0017 * amount

def bahrain_dinar_to_pkr(b_amount):
    return b_amount*586.18

def pkr_to_inr(amount):
    return 0.37 * amount

def inr_to_pkr(i_amount):
    return i_amount*2.69

def main():
    amount=int(input("enter:"))
    b_amount=int(input("Amount in bahrain dinar to pkr:"))
    i_amount=int(input("Amount of INR to PKr "))
    print(pkr_to_bahrain_dinar(amount))
    print(bahrain_dinar_to_pkr(b_amount))
    print(pkr_to_inr(amount))
    print(inr_to_pkr(i_amount))


main()




