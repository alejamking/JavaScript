from database import get_db, get_starting_airport, get_two_airports
from routes_config import ROUTES
import ui
from playerdata import create_player
import time

def main():

    while True:
        conn = get_db("python", "huihai")
        text = "Welcome to Show your Bag!\nScan, inspect, observer. Look for the things that don’t belong:\nsmuggled goods, restricted tech, banned items… or worse.\nOne mistake, and it’s not just your job on the line\n\n"
        for word in text:
            print(word, end="", flush=True)

            time.sleep(0.0001)
        player = create_player()

        print(f"\nHey! You’ve just received an invitation to your dream job in Australia! "
              f"\nThe problem is… you don’t have much money yet. Fortunately, you’re working as a luggage inspector at the airport. "
              f"\nBy taking new positions in airports a little closer to Australia, you can slowly make your way toward your final destination.\n")

        first_country = input("Enter the country that you want to start from (Finland, Sweden, Norway or Denmark):\n ").title()

        while first_country not in ROUTES:
                print("Invalid choice! You must choose Finland, Sweden, Norway or Denmark.")
                first_country = input("Enter the country that you want to start from:\n ").title()

        first_airport = get_starting_airport(conn, first_country)
        print(f"Your starting airport is: {first_airport[0]}, {first_airport[1]}")
        current_airport = first_airport

        player["location"] = current_airport

        route = ROUTES[first_country]
        current_index = 0

        # generates airports for the whole route
        airport_choices = {}
        for country in route:
            airports = get_two_airports(conn, country)
            if airports:
                airport_choices[country] = airports

        #sends airport_choices to ui.py
        result = ui.game_menu(player, conn, route, current_index, airport_choices)

        if result is False:  # if game ends
            print("\nGame over... Starting a new game...\n")
            continue  # start a new game





if __name__ == "__main__":
    main()
