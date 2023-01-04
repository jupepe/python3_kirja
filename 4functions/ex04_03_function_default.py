# Funktion oletusargumentit


def print_person(first_name="Robot", last_name='Tester', profession='test engineer'):
    print(f"{last_name}, {first_name} \t is a {profession}")


def get_person(first_name="Robot", last_name='Tester', profession='test engineer'):
    return f"{last_name:12s}, {first_name:12s}: {profession:12s}"


print_person("Pekko", "Lumberjack", "forester")
print_person("Unto", "Bricklayer", "bricklayer")

print_person(first_name="Unto", last_name="Bricklayer", profession="bricklayer")
print_person(profession="bricklayer", first_name="Unto", last_name="Bricklayer")

print_person("Pekka", "Lumberjack")

print_person(profession="forester", first_name="Pekka")

print_person()

print(get_person("Pekko", "Lumberjack", "forester"))
print(get_person("Unto", "Bricklayer", "bricklayer"))
