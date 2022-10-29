def euro_to_pkr(amount):
    return 0.0045 * amount

def pkr_to_euro(amount):
    return amount*220.61
def main():
    amount=int(input("enter amount:"))
    print(euro_to_pkr(amount))
    print(pkr_to_euro(amount))
main()

