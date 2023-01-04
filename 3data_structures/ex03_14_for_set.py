# set-esimerkkejä

sentence = "iterating over the 54 characters or words with python"
all_letters = list(sentence)
print(f"Letters to list: {all_letters}")


def split_sentence(w):
    return [ch for ch in w]


print(f"Split to list: {split_sentence(sentence)}")

letters = set(sentence)
print(f"Letters in sentence: {letters}")

print(f"Ind\t => \tLtr\thex_code")
for i, letter in enumerate(sorted(letters)):
    print(f"{i}\t => \t{letter} \t {hex(ord(letter))} \t {bin(ord(letter))}")
