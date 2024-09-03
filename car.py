class Car:
    def __init__(self, make, model, year):
        """
        Initialize a new Car instance.

        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Printing the car's information."""
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Example u
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()  # Output: Car Information: 2020 Toyota Camry
