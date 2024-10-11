import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_OF_PICKS = 6


def main():
    """get and display quick picks"""
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_picks = get_quick_picks(number_of_quick_picks)
    formatted_picks = format_quick_picks(quick_picks)
    for pick in formatted_picks:
        print(pick)


def get_quick_pick():
    """get one quick pick"""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBER_OF_PICKS))


def get_quick_picks(number_of_quick_picks):
    """get multiple quick picks"""
    return [get_quick_pick() for number in range(number_of_quick_picks)]


def format_quick_picks(quick_picks):
    """Formating the quick picks"""
    return [" ".join(f"{num:2}" for num in pick) for pick in quick_picks]


main()
