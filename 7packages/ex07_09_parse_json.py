# JSON-datan käsittely
import json


def create_json(dict_source):
    json_serialized = json.dumps(dict_source, indent=4)
    return json_serialized


def create_new_person():
    return {"first_name": "John", "last_name": "Smith",
            "address": {
                "street_address": "21 2nd Street",
                "city": "New York",
                "postal_code": "10021-3100"
            }, "phone": {
            "type": "mobile",
            "number": "055 54540054"},
            "employee": {
                "id": 22,
                "name": "dot com Oy"
            }}


def create_dictionary(json_person):
    return json.loads(json_person)


person = create_new_person()
json_person = create_json(person)
print(f"Serialisoitu JSON:\n{json_person}")

person2 = create_dictionary(json_person)
print(f"JSON luettu sanakirjaan:\n{person2}")
