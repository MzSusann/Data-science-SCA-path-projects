# SCA PROJECT

# 3RD WEEK PROJECT

#Exercise 1: Write a Python program to get the largest and lowest numbers from a list
list1 = [21,43,24,555,12,859]
print(max(list1))
print(min(list1))


#Exercise 2: Create a dictionary with the names and birthdays of at least five people. write a program that displays a person's birthday if found in the dictionary, and if not found, it should update the dictionary and add the birthday and name of the person. , Concepts to keep in mind:, Input(), function, dictionary

birthdays_deets = {
    "mzsusan" : {"Name": "Susan Onukogu", "Date": "3rd Dec"},
    "nancy2" : {"Name": "Nancy Ale", "Date": "24th May"},
    "amaka1" : {"Name": "Amaka Lea", "Date": "18th Sept"},
    "oscar45" : {"Name": "Oscar Micheal", "Date": "24th May"},
}

username = input('Enter username: ')
if username in birthdays_deets:
  print('Fullname:', birthdays_deets[username]['Name'], ', Birthday: ', birthdays_deets[username]['Date'])
else:
  # collect full name
  user_fullname = input('Enter full name: ')
  # collect date of birth
  user_dob = input('Enter date of birth: ')

  # create new entry for user in dictionary, using data collected already.
  birthdays_deets[username]= { 'Name': user_fullname, 'Date': user_dob }
  
  # print user details
  print('Fullname:', birthdays_deets[username]['Name'], ' Birthday: ', birthdays_deets[username]['Date'])

  print('entire object')
  print(birthdays_deets)
  
  # print a thank you message
  print('Thank you')




#Exercise 3: Write a program to update a tuple
ages = (20,23,35,46,12,61)
agesList = list(ages)

newage = [2 * item for item in agesList]
print(tuple(newage))


#Exercise 4: Write a Python program to create a union of sets

friends1 = {"Susan", "Nancy", "Amaka", "Oscar"}
friends2 = {"Joshh", "Martha", "Rita", "Susan"}
friends3 = {"Finn", "Sheila", "Fortune"}

new_friends = friends1.union(friends2,friends3)
print(new_friends)