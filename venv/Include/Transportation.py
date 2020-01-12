class Transportation:
    wheels = 0

    def __init__(self):
        self.wheels = -1

    def travel_one(self):
        print("Travelling on generic transportation")

    def travel(self, distance):
        for _ in range(distance):
            self.travel_one()

    def is_auto(self):
        return self.wheels == 4

class Bike(Transportation):

    def travel_one(self):
        print("Biking one mile")

class Car(Transportation):
    wheels = 4

    def travel_one(self):
        print("Driving one mile")

    def make_sound(self):
        print("VROOM")

class Ferrari(Car):
    pass

t = Transportation()
b = Bike()
c = Car()
f = Ferrari()
print(
isinstance(t, Transportation),

isinstance(b, Bike),
isinstance(b, Transportation),
isinstance(b, Car),
isinstance(b, Ferrari),

isinstance(c, Car),
isinstance(c, Transportation),

isinstance(f, Ferrari),
isinstance(f, Car),
isinstance(f, Transportation),

issubclass(Bike, Transportation),
issubclass(Car, Transportation),
issubclass(Ferrari, Car),
issubclass(Ferrari, Transportation),
issubclass(Transportation, Transportation),

b.travel(5),
c.is_auto(),
f.is_auto(),
b.is_auto(),
c.make_sound(),
c.travel(10),
f.travel(4))