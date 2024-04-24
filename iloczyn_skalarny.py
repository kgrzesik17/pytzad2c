import numpy

def dot(x, y):
    try:
        n = numpy.dot(x, y)
    except ValueError:
        print("Podane listy nie są takiej samej długości.")
        return

    return n

def make_array():
    try:
        n = int(input("Wprowadź długość listy: "))
    except ValueError:
        print("Niepoprawna wartość.")
        return

    a = []

    for i in range(1, n+1):
        try:
            x = int(input(f"Wprowadź {i} liczbę: "))
        except ValueError:
            print("Niepoprawna wartość.")

        a.append(x)

    return a