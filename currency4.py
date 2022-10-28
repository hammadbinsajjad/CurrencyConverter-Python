def dkk_to_pkr(d_amount):
    return 29.57 * d_amount

def pkr_to_dkk(amount):
    return amount*0.034
def main():
    d_amount=int(input("Enter Currency of Denmark"))
    amount=int(input("enter pkr:"))
    print(dkk_to_pkr(d_amount))
    print(pkr_to_dkk(amount),"Danish Krone")
main()

