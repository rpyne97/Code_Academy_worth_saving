## Search, add and edit libraries ##

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
key_to_check = "matcha"
#Use a 'try block' to check for key value of 'matcha'
try:
  print = caffeine_level[key_to_check]
except KeyError:
  print("Unknown Caffeine Level")
#Not there but you can add 'matcha' key with value 30 to caffeine_level dictionary
caffeine_level["matcha"] = 30

#More efficient way to search libraries is with get() function
#Returns 'NA' when key is not found
caffeine_level.get("matcha", NA)
'NA'
caffeine_level.get("espresso", "NA")
64

#Remove key:value item using the pop() function
etwas = caffeine_level.pop("espresso", "NA")
etwas
64
caffeine_level
{'chai': 40, 'decaf': 0, 'drip': 120}
#Remove value from a list and add to variable total_cost
total_cost = 0
total_cost += caffeine_level.pop("espresso", "NA")

## Extract information from libraries ##
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
num_exercises.keys()

#Create a dict_values object with dictionary values
num_exercises.values()

#Add to dic values to a new
total_exercises = 0
for i in num_exercises.values():
  total_exercises += i
print(total_exercises)

#Acess keys and values with .item() function
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for position, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + position +"s")


