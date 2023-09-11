from random import randint
from time import sleep


def main():
    first_side = input("Як назвати першу сторону монети? (За замовчанням \"Лик\"): ") or "Лик"
    second_side = input("Як назвати другу сторону монети? (За замовчанням \"Лік\"): ") or "Лік"
    coin = [first_side, second_side]
    coinflip(coin)


def coinflip(coin):
    print()
    sleep(1)
    print("Підкидаємо монету", end="")
    for i in range(3):
        sleep(1)
        print(".", end="")
    sleep(1)
    print("\n")
    result = coin[randint(0, 1)]
    print(f"Отже, результат: {result}!")


if __name__ == '__main__':
    main()
