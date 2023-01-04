# Privaatit ominaisuudet

class MyClass:
    def __init__(self, v1, v2):
        self._value1 = v1
        self._value2 = v2

    def get_values(self):
        return [self._value1, self._value2]


m = MyClass(21, 42)
print(f"{m.get_values()} ja {m._value1}")


class MyPrivClass:
    def __init__(self, v1, v2):
        self.__value1 = v1
        self.__value2 = v2
        self._value3 = 55

    def get_values(self):
        return [self.__value1, self.__value2]


m = MyPrivClass(21, 42)
print(f"{m.get_values()}")

print(f"viittaus {m._MyPrivClass__value1}, {m._MyPrivClass__value2}")

# print(f"{m.get_values()} and {m.__value1}")  # AttributeError: 'MyPrivClass' object has no attribute '__value1'
