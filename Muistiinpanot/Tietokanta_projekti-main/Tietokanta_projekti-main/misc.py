import random


def randomevent_boss1(player):
        #Randomgeneroitu tapahtuma, jossa pomo tulee juttusille

    print("Your boss comes to meet you in your lunchbreak\nHe asks for a favor after your shift is done\nA small baggage needs to be delivered to the city outskirts")
    print("Seems a bit shady")
    print("Will you accept the sidejob?(Yes or No)")
    while True:
        choice = input()
        if choice == "Yes":
            player["balance"] +=100
            print("Side job completed.")
            print("You earned extra 100€")
            return "randomevent_boss1"
        elif choice == "No":
            player["balance"] +=0
            print("Side job declined")
            return "randomevent_boss1"
        else:
            print("Invalid choice.")

#random tapahtumu aftereihin työpaikalla
def randomevent_boss2(player):
    print("Your boss and coworkers are going to after work tonight")
    print("They are eager to get out after a long streak of workdays")
    print("Your hottest coworker is also going")
    print("You are a little bit afraid to go, you start reminiscing last time you went")
    print("Shitfaced drunk you puked on another security officer")
    print("My god..")
    while True:
        print("Will you go?(Yes or No)")
        choice = input()
        if choice == "Yes":
            print("It all started well, but after a little while you started to wonder off to the dark side")
            print("Shot after shot you became more drunk")
            print("Your memory blacks out after two hours into the party")
            print("You wake up shaking and miserable")
            print("You need to call your boss that you are not coming today")
            print("What a disaster")
            player["day"] += 1
            player["balance"] -= 200
            print("200 euros had disappeared from your bankaccount")
            return "randomevent_boss2"
        if choice == "No":
            print("You kindly reject your coworkers company")
            print("Last time is sadly in your memory")
            print("You just saved a lot of money by staying home")
            return "randomevent_boss2"
        else:
            print("Invalid choice")


#randomtapahtuma jossa lentokentällä on lakko
def randomevent1(player):
    print("There a strike on the airport")
    print("You are not allowed to work so you spend the day\nin city spending a lot of money")
    print("50€ has dissappeared from your bank account")
    print("Hopefully the strike doesnt last long")
    player["balance"] -= 50
    print("")
    return "randomevent"

def trigger_random_event(player):
    events = [randomevent1, randomevent_boss1, randomevent_boss2]
    if random.random() < 0.1:
        result = random.choice(events)
        return result(player)
    return None
