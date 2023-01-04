# Ostosjono simulaatio

def shopping_queue_simulation(clients, new_clients):
    queue = []

    # asiakkaiden lisääminen jonoon
    while len(clients) > 0:
        queue.insert(0, clients.pop())

    print("Simulaatio alkaa.\nAsiakkaat ovat jonossa: ", queue)
    while queue:
        print("Palvellaan kassalla asiakasta ", queue.pop(0))

    # uusien asiakkaiden käsittely
    while len(new_clients) > 0:
        queue.insert(0, new_clients.pop())
    print("Uudet asiakkaat ovat jonossa: ", queue)
    while queue:
        print("Palvellaan kassalla asiakasta ", queue.pop(0))

    print("Jono on nyt tyhjä")


def main():
    clients = [('Pekka', 56.60), ('Matti', 70.35), ("Juhani", 90.65)]
    clients2 = [('Kaarina', 63.45), ('Anna', 43.60), ("Aino", 69.40)]
    shopping_queue_simulation(clients, clients2)


if __name__ == '__main__':
    main()
