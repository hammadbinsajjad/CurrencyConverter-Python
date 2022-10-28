def pkr_to_aed(amount):
    return 0.017 * amount

def pkr_to_russianruble(amount):
    return amount*0.28

def pkr_to_yuan(amount):
    return 0.033 * amount

def yuan_to_pkr(y_amount):
    return y_amount*30.46

def main():
    amount=int(input("enter:"))
    y_amount=int(input("Amount in yuan to pkr:"))
    print(pkr_to_aed(amount))
    print(pkr_to_russianruble(amount))
    print(pkr_to_yuan(amount))
    print(yuan_to_pkr(y_amount))
main()



