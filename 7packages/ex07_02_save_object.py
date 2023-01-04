# pickle-moduuli
import pickle

data1 = {'a': [1, 2, 3, 4],
         'b': ('information', 'Unicode str'),
         'c': None}
list1 = [1, 2, 3, 4, ['eight', 'nine', 'ten']]

output = open('files/dumb.dat', 'wb')

pickle.dump(data1, output)

pickle.dump(list1, output)

pickle.dump(10, output)

output.close()  # suljettava, jotta tiedot tallentuvat tiedostoon

file = open('files/dumb.dat', 'rb')

data1 = pickle.load(file)
print(data1)

data2 = pickle.load(file)
print(data2)

data3 = pickle.load(file)
print(type(data3))
print(data3)

file.close()
