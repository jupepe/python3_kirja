# set-tietorakenne

lista = [5, 2, 3, 4, 5, 4, 3, 2, 1, 'luku']
print(lista)
print(set(lista))

input_str = "ai että kun Python ohjelmointi sitten on mielenkiintoinen laji. Voi kun vaan osaisi enemmän."
lower_str = input_str.lower()
all_letters = set(lower_str)
print(all_letters)

for letter in sorted(list(all_letters)):
    print(f"'{letter}': {lower_str.count(letter)}")
