#Create a dictionary using a list comprehension
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
#Combine the two lists into a zipped list of pairs
zipped_drinks = zip(drinks, caffeine)
#Use list comprehension to convert zipped pairs into dictionary
#Takes each pair from zipped_drinks and names first element key and second element value
#Creates a key:value item in the drinks_to_caffeine dictionary
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffeine)