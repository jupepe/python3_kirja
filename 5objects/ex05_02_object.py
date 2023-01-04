# Konstruktori

class MyPython:

    def __init__(self, version):
        self.version = version

    def show_version(self):
        print(f"Version is {self.version}.")

    def set_version(self, version):
        self.version = version
        print("Setting new version")


my_python = MyPython("3.8")
my_python.show_version()
my_python.set_version("3.8.16")
my_python.show_version()

my_python2 = MyPython("3.10")
my_python2.show_version()
print(my_python2)
