"""
CP1404/CP5632 Practical - Suggested Solution
Test taxi
"""

from week_9.taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()