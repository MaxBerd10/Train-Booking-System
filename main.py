class Train:

    def __init__(self, train_id, name, seats):

        self.train_id = train_id
        self.name = name
        self.seats = seats
        self.booked_seats = []

    def book_seats(self, seat_number):
        if seat_number in self.booked_seats:

            print(f"Seat {seat_number} is already booked.")

        elif seat_number < 1 or seat_number > self.seats:

            print(f"Invalid seat number. Please choose a seat between 1 and {
                  self.seats}. ")

        else:
            self.booked_seats.append(seat_number)

            print(f"Seat {seat_number} successfully booked.")

    def display_seats(self):

        available_seats = [seat for seat in range(
            1, self.seats + 1) if seat not in self.booked_seats]

        print(f"Available seats: {available_seats}")

    def booking_status(self):
        print(f"Booked seats for {self.name}: {
              self.booked_seats if self.booked_seats else 'No seats booked yet.'} ")


class TrainBookingSystem:
    def __init__(self):
        self.trains = {

            101: Train(1012, "Express A", 10),
            102: Train(102, "Express B", 8),
            103: Train(103, "Express C", 12)
        }

    def display_trains(self):
        print("Available Trains:")

        for train_id, train in self.trains.items():
            print(f"Train ID: {train_id}, Name: {
                  train.name}, Seats:{train.seats}")

    def booked_seats(self, train_id, seat_number):
        if train_id in self.trains:
            self.trains[train_id].book_seats(seat_number)

        else:
            print("Invalid Train ID. Please try again.")

    def display_seats(self, train_id):

        if train_id in self.trains:
            self.trains[train_id].display_seats()

        else:
            print("Invalid Train ID. Please try again.")

    def booking_status(self, train_id):

        if train_id in self.trains:
            self.trains[train_id].booking_status()

        else:
            print("Invalid Train ID. Please try again.")


def main():
    system = TrainBookingSystem()

    while True:
        print("\nWelcome to the Train Booking System")
        print("1. View Trains")
        print("2. Book a Seat")
        print("3. Check Available Seats")
        print("4. View Booking Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.display_trains()

        elif choice == '2':
            train_id = int(input("Enter Train ID: "))

            seat_number = int(input("Enter Seat Number: "))

            system.booked_seats(train_id, seat_number)

        elif choice == '3':

            train_id = int(input("Enter Train ID: "))

            system.display_seats(train_id)

        elif choice == '4':

            train_id = int(input("Enter Train ID: "))

            system.booking_status(train_id)

        elif choice == '5':

            print("Thank you for using the Train Booking System.")

            break

        else:

            print("Invalid Train ID. Please try again.")


if __name__ == "__main__":

    main()
