class Calculator:
    def __init__(self):
        print("Simple Calculator !!!")

    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    def add(self, *args):
        return sum(args)

    def sub(self, x, y):
        return x - y

# Create object
obj = Calculator()
print(obj.add())
print(obj.sub(6, 4))  # This will call the first function with 2 parameters
print(obj.add(2, 3))  # This will call the second function with 2 parameters
print(obj.add(2, 3, 4))  # This will call the third function with 3 parameters
print(obj.add(2, 3, 4, 5))  # This will call the function with 4 parameters
print(obj.add(2, 3, 4, 5, 6))  # This will call the function with 5 parameters
print(obj.add(2, 3, 4, 5, 6, 7))  # This will call the function with 6 parameters
print(obj.add(2, 3, 4, 5, 6, 7, 8))  # This will call the function with 7 parameters