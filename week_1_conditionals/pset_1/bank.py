def main():
    """Отримуємо вітання та виводимо їх на екран"""
    greeting = input("Greeting: ")
    money = get_money(greeting)
    print(f"${money}")


def get_money(greeting):
    greeting = greeting.strip().lower()
    cash = 0

    if greeting == "hello" or greeting.split(",")[0] == "hello":
        return cash
    elif greeting[0] == 'h':
        cash = 20
        return cash
    else:
        cash = 100
        return cash


main()
