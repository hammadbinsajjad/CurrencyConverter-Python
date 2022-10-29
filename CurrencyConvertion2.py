def lira_to_pkr(amount):
    return 11.91 * amount

def pkr_to_lira(amount):
    return amount*0.084
def main():
    amount=int(input("enter amount:"))
    print(lira_to_pkr(amount))
    print(pkr_to_lira(amount))
main()

