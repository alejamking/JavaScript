import time
import sys

def ticker(teksti, leveys=60, nopeus=0.08, toistot=1):
    teksti = " " * leveys + teksti + " " * leveys
    for _ in range(toistot):
        for i in range(len(teksti) - leveys):  # HUOM! ei +1
            ikkuna = teksti[i:i+leveys]
            sys.stdout.write("\r" + ikkuna)
            sys.stdout.flush()
            time.sleep(nopeus)
    print("\r" + " " * leveys, end="\r")


def print_news_by_country(current_country):
    print("\n")

    if current_country == "Finland":
        print("News from Finland:")
        ticker("Plane collides with a reindeer near Kuusamo Airport – Santa raises concerns about air travel safety.")
    elif current_country == "Germany":
        print("News from Germany:")
        ticker("Berlin Airport closed after tourists’ bratwursts caused a security scare – Sausages looked like missiles on X-Ray.")
    elif current_country == "Romania":
        print("News from Romania:")
        ticker("Planes take off half-empty in Romania – Yesterday’s wine fest was to blame")
    elif current_country == "Pakistan":
        print("News from Pakistan:")
        ticker("World’s highest ATM is located above the clouds in Pakistan – People joke they need a plane just to withdraw cash.")
    elif current_country == "Malaysia":
        print("News from Malaysia:")
        ticker("A visually impaired grandma mistook her husband for a monkey, and the monkey accidentally got a seat on the plane – Passengers reported it followed the seatbelt instructions better than anyone else.")
    elif current_country == "Sweden":
        print("News from Sweden:")
        ticker("Passenger’s luggage fails the security check because it was full of IKEA meatballs – Security team wraps up the day well-fed.")
    elif current_country == "France":
        print("News from France:")
        ticker("Chaos erupts at Paris-Charles de Gaulle airport – Fans seen chasing Kylian Mbappe")
    elif current_country == "Croatia":
        print("News from Croatia:")
        ticker("Finnish tourists are confused – the water is crystal clear in Baska Voda ")
    elif current_country == "Turkmenistan":
        print("News from Turkmenistan:")
        ticker("Turkmenistan Airlines reports record punctuality – Experts note it helps when there are almost no passengers")
    elif current_country == "Thailand":
        print("News from Thailand:")
        ticker("Flight attendants handed out Aloe Vera on the Phuket-Helsinki flight because the plane was full of sunburned Finnish tourists.")
    elif current_country == "Norway":
        print("News from Norway:")
        ticker("Norwegian Airlines struggle as citizens choose skis over flights")
    elif current_country == "Ireland":
        print("News from Ireland:")
        ticker("Flight delayed at Dublin airport after a Shetland pony is found in a passenger’s carry-on – Staff say: ‘No worries, the pony got its own seat.’")
    elif current_country == "Poland":
        print("News from Poland:")
        ticker("Tourists mistake Malbork Castle in Poland for airport terminal – Ask where to check in")
    elif current_country == "Uzbekistan":
        print("News from Uzbekistan:")
        ticker("Flights cancelled in Uzbekistan because of an earthquake warning ")
    elif current_country == "Vietnam":
        print("News from Vietnam:")
        ticker("Vietnam’s streets evolve as wings are tested on scooters.")
    elif current_country == "Denmark":
        print("News from Denmark:")
        ticker("World’s first motorized LEGO airplane built in Billund – But can it stay in one piece?")
    elif current_country == "Belgium":
        print("News from Belgium:")
        ticker("Brussels flight serves chocolate and waffles – The restroom line quickly grows.")
    elif current_country == "Slovakia":
        print("News from Slovakia:")
        ticker("Finnish and Slovakian hockey fans clash at the airport – Security measures are taken: The fans are put in different flights")
    elif current_country == "Tajikistan":
        print("News from Tajikistan:")
        ticker("1000 kilograms of salt confiscated from tourists – The salt originated from Sarikol Salt Mountain")
    elif current_country == "Philippines":
        print("News from Philippines:")
        ticker("Airline in the Philippines considers adding ‘Filipino Time’ to official timetable to avoid constant delay announcements")
    elif current_country == "Australia":
        print("News from Australia:")
        ticker("World’s best baggage inspector finally finds a new job in dream destination – It’s about time")
    else:
        print("No news available for this country.")