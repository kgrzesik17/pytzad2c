def exponentiation():
    try:
        x = float(input("Wprowadź podstawę potęgi: "))
        y = float(input("Wprowadź wykładnik potęgi: "))
    except ValueError:
        print("Niepoprawna wartość.")
        return
    
    try:
        n = x ** y
    except OverflowError:
        print("Wynik jest zbyt duży.")
        return
    except ZeroDivisionError:
        print("Wartość nie może równać się zero.")
        return
    
    return n

    
print(exponentiation())