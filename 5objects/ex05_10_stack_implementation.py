# Esimerkki: Oman tietorakenneluokan toteutus

class StackImplementation:
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if item is None:
            raise ValueError("Item pushed was None")
        self._elements.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop because stack is empty")
        return self._elements.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek because stack is empty")
        return self._elements[-1]

    def size(self):
        return len(self._elements)


book_stack = StackImplementation()
book_stack.push("Python Cookbook")
book_stack.push("Learn Python")
book_stack.push("Python with AI")
book_stack.push("Fluent Python")
print(f"Pinon huippu: {book_stack.peek()}")
print(f"Pinon koko: {book_stack.size()}")
book_stack.pop()
book_stack.pop()
book_stack.push("Data Analysis using Python")
print(f"Pinon huippu: {book_stack.peek()}")
print(f"Pinon koko: {book_stack.size()}")

while not book_stack.is_empty():
    print(book_stack.pop())

try:
    book_stack.pop()
except IndexError as err:
    print(err)
if not book_stack.is_empty():
    print(book_stack.pop())
try:
    print(f"Pinon koko: {book_stack.peek()}")
except IndexError as err:
    print(err)

print(f"Onko pino tyhjä: {book_stack.is_empty()}")
