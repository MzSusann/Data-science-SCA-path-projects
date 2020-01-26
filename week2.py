#SCA PROJECT

#2ND WEEK PROJECTS

#Exercise 1: 99 Bottles.  Create a program that prints out every line to the song "99 bottles of beer on the wall."Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead. Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

bottlecount = range(99, 0, -1)

for count in bottlecount:
  sec_count = count - 1
  if (count == 2 and sec_count == 1): #When bottles is 2 and then reduced to 1
      print(count, " bottles of beer on the wall", count, "bottles of beer. Take one down and pass it around", sec_count, "bottle of beer on the wall." )
  elif (count ==1 and sec_count ==0): #When bottle is 1 and then reduced to 0
    print(count, " bottle of beer on the wall", count, "bottle of beer. Take one down and pass it around", sec_count, "bottle of beer on the wall." )
  else:
      print(count, " bottles of beer on the wall", count, "bottles of beer. Take one down and pass it around", sec_count, "bottles of beer on the wall.")


#Exercise 2: Guess the Number; The Goal: This project uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.Concepts to keep in mind: Random function, Variables, Integers, Input/Output,Print, loops

import random

computerGuess = random.randint(0, 6)

#print(computerGuess)
try: 
  userGuess = int(input("Enter your guessed number between 0 and 6 (note: whole number): "))

  if userGuess < computerGuess:
    dif = computerGuess - userGuess
    print(userGuess, " is less than the Computer Guess, The right guess was ", computerGuess, ".", "You were close, The difference was ", dif)
  elif userGuess > computerGuess:
    diff = userGuess - computerGuess
    print(userGuess, " is greater than the Computer Guess, The right guess was ", computerGuess, ".", "You were close, The difference was ", diff)
  else:
    print(userGuess, " is correct, You got the guess right ", computerGuess)
except ValueError:
  print("Not an integer! Try again.")



# Exercise 3: Password Generator
#Write a programme, which generates a random password for the user. Ask the user how long they want their password to be, 
#and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers 
#and symbols. The password should be a minimum of 6 characters long.

import string
import random 


length_of_password = int(input("How long do you want your password?: "))
user_letters = int(input("How many letters do you want in your password?: "))
user_numbers = int(input("How many numbers do you want in your password?: "))


if(user_letters + user_numbers == length_of_password):
  def randomStrings(desiredLengthStr):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(desiredLengthStr))

  def randomDigits(desiredLengthDgt):
    """Generate a random digit of fixed length """
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(desiredLengthDgt))

  
  randompassword = randomStrings(user_letters)  + randomDigits(user_numbers)

  splittedString = list(randompassword)
  print(splittedString)

  random.shuffle(splittedString)
  joinedString = ''.join(splittedString) #using "".join() function to join the string without any seperator 

  print(joinedString)

else:
  print("Kindly confirm the addition of the number of letters and numbers specified is equal to the total length of the passport as specified")


