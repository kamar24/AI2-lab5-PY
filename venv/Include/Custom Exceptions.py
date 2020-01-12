class OutOfRangeError(ValueError):
    pass

def get_age():
    while True:
        try:
            age = input("How old are you?")
            age = int(age)
            if age < 0:
                raise OutOfRangeError
            if age > 123:
                raise Exception("Age", age, "out of range")
        except OutOfRangeError:
            print("Invalid integer input.")
        except ValueError:
            print("Invalid integer input.")

        else:
            return False
        finally:
            print(age)