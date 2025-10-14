import gc

class TestClass:
    def __init__(self):
        print('Object created')

obj = TestClass()

lst = [obj]

del obj

gc.collect()

print("Garbage collection completed")