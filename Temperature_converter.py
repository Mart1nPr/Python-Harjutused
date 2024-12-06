# Temperature converter
# 12/06/2024

choice = int(input("Write 1 for (Celsius -> Fahrenheit) or 2 for (Fahrenheit) -> Celsius): "))
match choice:
    case 1:
        # F = C × (9/5) + 32
        Celcius = int(input("Enter temperature in Celcius: "))
        C = Celcius
        F = C * (9/5) + 32
        print(f"{C} in Celcius is {F} in Fahrenheit.")
    case 2:
        # C = (F - 32) × 5/9
        Fahrenheit = int(input("Enter temperature in Fahrenheit: "))
        F = Fahrenheit
        C = (F - 32) * 5/9
        print(f"{F} in Fahrenheit is {C} in Celcius.")
    case _:
        print("Enter 1 or 2")