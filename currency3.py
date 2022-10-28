def takka_to_pkr(t_amount):
    return 2.18 * t_amount

def pkr_to_takka(amount):
    return amount*0.46
def main():
    t_amount=int(input("enter"))
    amount=int(input("enter2:"))
    print(takka_to_pkr(t_amount))
    print(pkr_to_takka(amount))
main()

