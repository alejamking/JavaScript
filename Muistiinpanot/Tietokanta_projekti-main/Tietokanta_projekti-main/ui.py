import random
import news
from geopy.distance import geodesic
import items
from misc import trigger_random_event, randomevent_boss2, randomevent_boss1


def calculate_distance_and_price(current_airport, next_airport, price_per_km=0.06):
    # Calculate price of flight ticket based on distance and rate per km
    distance = geodesic(
        (current_airport[2], current_airport[3]), # Current airport lat/lon
        (next_airport[2], next_airport[3])  # Next airport lat/lon
    ).km
    # Calculate price of flight ticket based on distance and rate per km
    price = round(distance * price_per_km, 2)
    # Return the rounded distance (km) and price (€)
    return round(distance, 1), price

def fly_menu(player, conn, route, current_index, airport_choices):
    # Check if the player is already at the final destination
    if current_index >= len(route) - 1:
        print("\nYou are already at your final destination Australia!")
        return player["location"], current_index

    # Get the next country in the travel route
    next_country = route[current_index + 1]
    # Get the pre-saved airports for that country
    next_airports = airport_choices.get(next_country, [])

    # If no airports found, skip this country
    if not next_airports:
        print(f"\nNo valid airports found in {next_country}. Skipping this destination.")
        return player["location"], current_index + 1

    # Print the available airport options in the next country
    print(f"\nNext destination options in {next_country}: ")
    for i, airport in enumerate(next_airports, 1):
        distance, price = calculate_distance_and_price(player["location"], airport)
        print(f"{i}, {airport[0]} ({airport[1]}) - {distance} km, Price: {price} €")

    # Ask the player to choose an airport
    choice = input("Choose your next airport (1 or 2): ")
    if choice not in ["1", "2"]:
        print("Invalid choice, staying at current airport.")
        return player["location"], current_index

    # Select the chosen airport
    next_airport = next_airports[int(choice) - 1]
    distance, price = calculate_distance_and_price(player["location"], next_airport)

    # Check if player has enough money to fly
    if player["balance"] >= price:
        player["balance"] -= price
        player["location"] = next_airport
        player["day"] += 1
        current_index += 1
        balance = float(player['balance'])
        print(f"\nYou flew to: {next_airport[0]}, {next_airport[1]}")
        print(f"Flight cost: {price} €. Remaining balance: {balance:.2f} €")
        # Check if this is the final destination
        if current_index == len(route) - 1:
            balance = float(player['balance'])
            print("\nCongratulations! You have reached your final destination: Australia!")
            print(f"Days traveled: {player['day']}")
            print(f"Final balance: {balance:.2f} €")
            news.print_news_by_country("Australia")
            quit()
        # Return the new location and updated index
        return next_airport, current_index
    else:
        # Not enough money to fly
        print("\nNot enough money for this flight!")
        return player["location"], current_index

def work_message():
    # List of possible random work-related messages
    messages = [
        "\n\nAnother shitty day ahead...",
        "\n\nIt's a nice day to go to work. I need to earn more money.",
        "\n\nRainy day ahead. The bus is full of smelly people.\nHow great..",
        "\n\nStepped on dogshit when walking to work. I ***ing hate dogs",
        "\n\nWhy do I need to suffer like this. Waking up every morning for nothing\nWish I could get out of here",
        "\n\nIm so tired. And the day just started",
        "\n\nIm late again. Hope nobody notices",

    ]
    return random.choice(messages)

def work_day(player,connection):
    round_history = []
    player["balance_at_start"] = player["balance"]

    print(work_message())
    print("\n--- Work Day Begins ---")
    print("\nYou will see descriptions of five items inside luggage.\n"
          "Your task is to decide whether the bag is allowed or denied for the flight.\n"
          "A bag is denied if it contains one or more forbidden items.\n"
          "Dangerous items must never be allowed through, but small amounts of liquids "
          "and small sharp objects are acceptable.\n"
          "You will get a penalty if you answer wrong. After you get five penalties the game is over.\n"
          "Each day, you need to check a total of five bags.\n\n")

    base_salary = player["salary"]

    #checking for randomevents happening
    event=trigger_random_event(player)
    #if random event is a strike in the airport, workday ends
    if event == "randomevent1":
        return True

    total_rounds = 5
    for i in range(1, total_rounds + 1):  # 5 bags
        ongoing = items.play_round(i,total_rounds, player, round_history, connection)
        if not ongoing:  # game over inside play_round
            print("Game over! Thanks for playing")
            return False
    # If all 5 bags checked successfully:
    balance_change = player["balance"] - player["balance_at_start"]
    total_earnings = base_salary + balance_change

    player["balance"] += base_salary
    player["day"] += 1

    print(f"\nWork day complete! ")
    print(f"Base salary: {base_salary} € and performance result: {balance_change:.2f} €")
    print(f"Total earned today: {total_earnings:.2f} €")
    print(f"New balance: {player['balance']:.2f} €")
    print(f"Day {player['day']} begins.")

    if random.random() < 0.05:
        event = random.choice([randomevent_boss1, randomevent_boss2])
        event(player)

    input(f"\nPress Enter to return to main menu...")
    return True

def news_menu(player):
    # Show current news for the country where the player is located
    news.print_news_by_country(player["location"][1])
    input("Press enter to continue")

def quitgame_menu():
    # Print a goodbye message and quit the game
    print("\nThanks for playing!")
    quit()

def show_menu(player, conn, route, current_index, airport_choices):
    # Display the main player status menu
    print("\n" + "="*40)
    print(f"Alias: {player['name']}")
    print(f"Day {player['day']} ")
    print(f"Balance: {player['balance']:.2f} €")
    print(f"Location: {player['location'][0]}, {player['location'][1]}")
    print(f"Penalties: {player['penalties']} / 5")
    print("="*40)

    if current_index < len(route) - 1:
        next_country = route[current_index + 1]
        next_airports = airport_choices.get(next_country, [])

        if next_airports:
            print(f"\nNext destination options in {next_country}: ")
            for i, airport in enumerate(next_airports, 1):
                distance, price = calculate_distance_and_price(player["location"], airport)
                print(f"{i}, {airport[0]} ({airport[1]}) - {distance} km, Price: {price} €")
        else:
            print(f"\nNo valid airports found in {next_country}.")

    print("\nAvailable actions:")
    print("1. Go to work")
    print("2. Check current news")
    print("3. Fly to next destination")
    print("4. Quit game (game will not be saved)")

def game_menu(player, conn, route, current_index, airport_choices):
    # Main game loop
    while True:
        show_menu(player, conn, route, current_index, airport_choices)
        choice = input("Choose action: ")
        if choice == "1":
            result = work_day(player, conn)
            if not result:
                return False
        elif choice == "2":
            news_menu(player)
        elif choice == "3":
            player["location"], current_index = fly_menu(player, conn, route, current_index, airport_choices)
        elif choice == "4":
            quitgame_menu()
        else:
            print("Invalid choice.")
