#count letters of a string without using len() function
def get_length(string):
  counter = 0
  for letter in string:
    counter += 1
  return counter

print(get_length("test"))

#make a list of unique shared letters between two strings
def common_letters(string_one, string_two):
  matches = []
  for i in string_one:
    if i in string_two and i not in matches:
      matches.append(i)
  return matches

matches = common_letters("manhattan", "san francisco")

def username_generator(first_name, last_name):
  if len(first_name) > 4:
    username = first_name[:4]
  else:
    username = first_name
  if len(last_name) > 3:
    username += last_name[:3]
  else:
    username += last_name
  return username

def password_generator(username):
 password = ""
 for letter in range(len(username)):
   password += username[letter-1]
 return password

password_generator(username_generator("Abe", "Simpson"))

#Split a first and last name then make new list with last name only
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
for author in author_names:
  author_last_names.append(author.split()[-1])
print(author_last_names)



