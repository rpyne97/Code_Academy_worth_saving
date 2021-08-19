# Start with two lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# Dictionary comprehension with zip() function to convert two lists to a dictionary
letters_to_points = {key:value for key, value in zip(letters, points)}
# Add a key:value pair to the dictionary
letters_to_points[" "] = 0
# Create a function to score words using the dictionary
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter, 0) # .get() allows for the option to return a 0 when a key is not found
  return point_total
# Test it
brownie_points = score_word("BROWNIE")
print(brownie_points)
# Now calculate scores for each player
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi":["ERASER","BELLY","HUSKY"], "Prof Reader":["ZAP","COMA","PERIOD"]}
# Add more words to a player already in the library
player_to_words["player1"].append("KARTOFFEL")
# Add a new player with a set of words
player_to_words["player2"].append("KARTOFFEL", "LIEBLING", "METHODE")

# Create a new library as a global variable outside the for loop that will hold player point totals
player_to_points = {}
# For loop iterates through the player_to_words library
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
print(player_points)

## Now convert that last nested for loop into a function
def update_point_total():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

