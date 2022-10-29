def won_to_pkr(amount):
    return 0.16 * amount

def pkr_to_won(amount):
    return amount*6.42
def main():
    amount=int(input("enter amount:"))
    print(won_to_pkr(amount))
    print(pkr_to_won(amount))
main()

