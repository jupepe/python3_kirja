# Koodilohkot

for i in range(10):
    print(i)

for i in range(10):
    if i % 2 == 1:
        print("Pariton luku:", end="\t")
        print(i)

for i in range(10):
    if i % 2 == 1:
        print("Pariton luku:   ", end="\t")
        print(i)
    else:
        print("Parillinen luku:", end="\t")
        print(i)


def show_lang(msg):
    if msg is None:
        print(f"Tervehdyssanaa ei annettu lainkaan")
    elif msg == "hei" or msg == "terve":
        print(f"Tervehdys '{msg}' on suomea")
    elif msg == "hello" or msg == "hi":
        print(f"Tervehdys '{msg}' on englantia")
    else:
        print(f"Mitä kieltä tämä '{msg}' on?")


def main_program():
    show_lang("hello")
    show_lang("terve")
    show_lang("somettaja")
    show_lang(None)


main_program()
