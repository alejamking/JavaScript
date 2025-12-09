import random
import time
from playerdata import create_player
from database import get_items

def add_luggage(connection):
    items = get_items(connection)

    weights = [max(1, 6 - item["danger_level"]) for item in items]

    chosen = []
    available_items = items[:]
    available_weights = weights[:]

    for _ in range(min(5, len(available_items))):
        total = sum(available_weights)
        r = random.uniform(0, total)
        upto = 0
        for i, w in enumerate(available_weights):
            upto += w
            if r <= upto:
                chosen_item = available_items.pop(i)
                available_weights.pop(i)
                chosen.append(chosen_item)
                break
    return chosen



def show_bag(bag):
    text = "Scanning luggage..\nThe bag contains:\n"
    for char in text:
        print(char,end="", flush = True)
        time.sleep(0.09)
    for thing in bag:
        print(f" - {thing['description']}")

def ask_decision():
    while True:
        choice = input("\nDo you let the bag through security? [allow/deny]: ").strip().lower()
        if choice in ("allow", "a", "yes", "y"):
            return True
        if choice in ("deny", "d", "no", "n"):
            return False
        print("Please type 'allow' or 'deny'.")

#tarkistaa onko matkattavaroissa sallittuja tavaroita
def is_safe_luggage(bag):
    for item in bag:
        if item["security_class"]==1:
            return False
    return True


def play_round(round_number, total_rounds, player, round_history, connection):
    print(f"\n--- Bag {round_number} ---")
    bag = add_luggage(connection)
    show_bag(bag)
    allow = ask_decision()

    penalty_count = player.get("penalties", 0)
    game_over = False
    reasons = [] #kerätään syyt listaan

    #taso 5 esineet --> välitön game over
    danger_items = [item["name"] for item in bag if item["danger_level"] == 5]
    if allow and danger_items:
        reasons.append(f"Contained danger level 5 items: {', '.join(danger_items)}")
        print("\nGAME OVER: You allowed a bag that contained a danger level 5 item.")
        game_over = True

    # kielletyt esineet(ei taso 5)
    suspicious_items = [item["name"] for item in bag if item["security_class"] == 1 and item["danger_level"] < 5]
    if allow and suspicious_items and not game_over:
        reasons.append(f"Suspicious items allowed: {', '.join(suspicious_items)}")
        penalty_count += 1
        print("Warning! You let a suspicious item through the airport security! A penalty will be applied!")
        if penalty_count>=5:
            print("\nGAME OVER! You have received 5 penalties.\nYou are a threat to aviation")
            game_over = True



    # turvallisen laukun turha kieltäminen
    if not allow and is_safe_luggage(bag) and not game_over:
        reasons.append("Denied a completely safe bag")
        penalty_count += 1
        print("Why didnt you let that through a completely safe bag?")
        print("You have received a penalty")
        if penalty_count >= 5:
            print("\nGAME OVER! You have received 5 penalties.\nYou are a threat to aviation")
            game_over = True

    if not game_over:
        if reasons:  #päätös oli väärä
            player["balance"] -= 10
            print(f"Penalty: -10 €. New balance: {player['balance']:.2f} €")
        else:  #päätös oli oikein
            player["balance"] += 20
            print(f"Bonus: +20 €. New balance: {player['balance']:.2f} €")

    # oikein tarkastettu laukku
    if not reasons and not game_over:
        print("Correct! The bag was " + ("allowed" if allow else "denied") + ".")


    #laukun sisältö
    print("Items in the bag were:")
    for item in bag:
        print(" -", item["name"])

    #jos syitä on, tulostetaan ne
    if reasons:
        print("reason(s):")
        for r in reasons:
            print(" -", r)

    #päivitetään pelaajan tiedot ja historia
    round_info = {
        "round": round_number,
        "allowed": allow,
        "penalty_count": penalty_count,
        "bag": bag,
    }
    round_history.append(round_info)
    player["penalties"]=penalty_count

    if game_over:
        return False

    if round_number < total_rounds:
        input("\nPress Enter to continue to the next bag...")
    else:
        input("\nPress Enter to end your work day... ")
    return True




if __name__ == "__main__":
    player = create_player()
    player["penalties"] = 0
    round_history = []

    total_rounds = 5
    for i in range(1, total_rounds + 1):
        ongoing = play_round(i, total_rounds, player, round_history, connection)
        if not ongoing:
            break
    else:
        print("\nCongratulations! You successfully checked 5 bags.")
