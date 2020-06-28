class Flight:
    counter = 1

    def __init__(self, origin, destination, duration):
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_informations(self):
        print(self.origin)
        print(self.destination)
        print(self.duration)
        print("Passengers: ")
        for passenger in self.passengers:
            print(passenger.name)

    def add_passagers(self, p):
        self.passengers.append(p)
        p.filght_id = self.id


class Passenger:
    def __init__(self, name):
        self.name = name


def main():
    # create a instance of this class
    f = Flight(origin="New York", destination="Paris", duration=540)

    Jairo = Passenger('Jairo')
    Hugo = Passenger('Hugo')
    Joaquim = Passenger('Joaquim')
    Pedro = Passenger('Pedro')

    f.add_passagers(Jairo)
    f.add_passagers(Hugo)
    f.add_passagers(Joaquim)
    f.add_passagers(Pedro)

    f.duration += 10

    f.print_informations()


if __name__ == "__main__":
    main()
