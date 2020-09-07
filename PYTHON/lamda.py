people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# This method is a function that will sort each object by cf name field values:
# def f(person):
#     return person["name"]
# people.sort(key=f)

# Lambda expression - alternative method:
people.sort(key=lambda person: person["name"])

print(people)
