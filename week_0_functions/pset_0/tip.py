def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """Приймає суму, прибирає символ '$' та повертає як float"""
    
    d = d.replace("$", "")
    d = float(d)
    d = d / 100

    return d


def percent_to_float(p):
    """Приймає відсоток, прибирає символ '%' та повертає як float"""
    
    p = p.replace("%", "")
    p = float(p)

    return p


main()
