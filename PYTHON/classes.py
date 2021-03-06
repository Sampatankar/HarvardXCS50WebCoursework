# Part1 - Classes in OOP:
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# p = Point(2, 8)
# print(p.x)
# print(p.y)

# Part 2: Flight booking system example:
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    # success = flight.add_passenger(person) - we can put this entire condition into the if statement, rather than through success var:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")
