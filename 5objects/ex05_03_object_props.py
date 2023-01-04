# object-luokan metodit
class MyPython:
    def __init__(self, version):
        self.version = version

    @staticmethod
    def show():
        print("I'm a MyPython class")
        # self.version  # NameError: name 'self' is not defined


my_python = MyPython("3.8")
my_python.show()
MyPython.show()


class MyPython:
    def __init__(self, version):
        self.version = version

    def show_version(self):
        print(f"Version is {self.version}.")

    def set_version(self, version):
        self.version = version
        print("Setting new version")

    def __str__(self):
        return f"Version is {self.version}."

    def __repr__(self):
        return f'MyPython("{self.version}")'

    @staticmethod
    def show():
        print("I'm a MyPython class")
        # self.version  # NameError: name 'self' is not defined


my_python = MyPython("3.8")
print(my_python)
my_python.set_version("3.8.16")
print(my_python)  # kutsuu __str()__
print(repr(my_python))  # kutsuu __repr()__

my_python2 = MyPython("3.10")
my_python2.show()
print(my_python2)
print(repr(my_python2))
print(my_python2)

print(my_python.__getattribute__("version"))
print(my_python.__setattr__("version", "3.10.5"))
print(my_python)

print(my_python.__delattr__("version"))
try:
    print(my_python)  # AttributeError: 'MyPython' object has no attribute 'version'
except AttributeError as exp:
    print(f"AttributeError: {exp}")

print(my_python.__doc__)
print(my_python.__dict__)
print(my_python.__module__)
print(my_python.__hash__())


class MyPython:
    def __init__(self, version):
        self.version = version

    def show_version(self):
        print(f"Version is {self.version}.")

    def set_version(self, version):
        self.version = version
        print("Setting new version")

    def __str__(self):
        return f"Version is {self.version}."

    def __repr__(self):
        return f'MyPython("{self.version}")'

    def __eq__(self, other):
        return self.version.__eq__(other.version)

    def __ne__(self, other):
        return self.version.__ne__(other.version)

    def __le__(self, other):
        return self.version.__le__(other.version)

    def __lt__(self, other):
        return self.version.__lt__(other.version)

    def __gt__(self, other):
        return self.version > other.version  # tai __gt__(other)

    def __ge__(self, other):
        return self.version >= other.version  # tai __ge__(other)


my_python = MyPython("3.10.1")
my_python2 = MyPython("3.10.5")
my_python3 = MyPython("3.10.1")
print(my_python == my_python3)
print(my_python.__eq__(my_python3))
print(my_python >= my_python2)
print(my_python3.__ne__(my_python2))
