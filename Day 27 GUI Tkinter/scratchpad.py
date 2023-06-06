def add(*args):
    result = 0
    for n in args:
        result += n
    return result


total = add(1, 2, 3, 4, 5, 6, 7, 8, 9)


# print(total)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", seats="4")
print(my_car.model)
print(my_car.make)
print(my_car.seats)
