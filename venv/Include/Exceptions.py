def get_age():
    while True:
        try:
            age = int(input("How old are you?"))
            if age < 0:
                raise ValueError
            if age > 123:
                raise Exception("Age", age, "out of range")
            print(age)
            return False
        except ValueError:
            print("Invalid integer input.")

get_age()
