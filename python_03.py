class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_by_city(self, city):
        matching_flights = []
        for flight in self.flights:
            if city in (flight.source, flight.destination):
                matching_flights.append(flight)
        return matching_flights

    def search_flights_from_city(self, source_city):
        matching_flights = []
        for flight in self.flights:
            if flight.source == source_city:
                matching_flights.append(flight)
        return matching_flights

    def search_flights_between_cities(self, source_city, dest_city):
        matching_flights = []
        for flight in self.flights:
            if flight.source == source_city and flight.destination == dest_city:
                matching_flights.append(flight)
        return matching_flights

def main():
    flight_table = FlightTable()

   
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Search Flights:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_flights_by_city(city)
    elif choice == 2:
        source_city = input("Enter the source city: ")
        result = flight_table.search_flights_from_city(source_city)
    elif choice == 3:
        source_city = input("Enter the source city: ")
        dest_city = input("Enter the destination city: ")
        result = flight_table.search_flights_between_cities(source_city, dest_city)
    else:
        print("Invalid choice")
        return

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
