#täällä säilytetään playerdata
def create_player():
    name = input("Please enter your name: ")
    # Create a dictionary with the player's starting stats
    player = {
        "name": name,
        "balance": 2000,
        "salary": 100,
        "location": None,
        "day": 1,
        "penalties": 0,
    }
    # Return the player dictionary
    return player