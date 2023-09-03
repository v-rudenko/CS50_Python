def main():
    mass = int(input("m: "))
    energy = calculate_energy(mass)
    print(f"E: {energy}")

def calculate_energy(m):
    """Вираховує енергію за вказаною масою"""
    c = 300000000
    E = m * c ** 2
    return E
main()
