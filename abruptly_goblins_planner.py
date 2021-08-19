# Create empty list (of dictionaries) for people attending game night
gamers = []
# Create a function to add gamer name and availability to gamer_list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")
kimberly = {"name":"Kimberly Warner", "availability":["Mondays","Tuesdays","Wednesdays"]}

# Use add_gamer() function to kimberly dictionary to gamers_list
add_gamer(kimberly, gamers)
# Add additional gamer information
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Now gamer is a list of dictionaries. Each dictionaory is an element in the list
print(gamers)
# Note an issue with the first dictionary - Mondays instead of Monday and last dictionary -
# Delete and add the corrected library by index number
len(gamers)
del gamers[0]
del gamers[9]
add_gamer({"name":"Kimberly Warner", "availability":["Monday","Tuesday","Wednesday"]})

# Now create a dictionary to store availability by day
def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }
# Save the frequency table as count_availability object
count_availability = build_daily_frequency_table()
# Create a function to iterate through each day in the gamer's availability and add to occurence to availability_frequency
def calculate_availability(gamers_list,availability_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            availability_frequency[day]+=1
# Call calculate_availability() to fill the frequency table - count_availability
calculate_availability(gamers,count_availability)

# Create a function to find best night to play
def find_best_night(availability_table):
    best_availability = 0
    # day = key and value = availability in dictionary availability_table
    for day, availability in availability_table.items():
        # If the integer for availability is greater than the current best_availability integer
        if availability > best_availability:
            # Then best_night becomes the day (key) for this day (value) and
            best_night = day
            # The best_availabilty becomes the day (value)
            best_availability = availability
    return best_night

# Call find_best_night() function
game_night = find_best_night(count_availability)
# Thursday has the most available players
print(game_night)

# make a list of all of the people who are available that night
def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)


# form email to send to each of the participants
form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

#
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))


send_email(attending_game_night, game_night, "Abruptly Goblins!")
