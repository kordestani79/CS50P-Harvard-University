def main():
    amount_due = 0

    while amount_due < 50:
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            amount_due += coin
            print("Amount Due:", 50 - amount_due)
        else:
            print("Amount Due: 50")

    change_owed = abs(amount_due - 50)
    print("Change Owed:", change_owed)

if __name__ == "__main__":
    main()
