# Title the story with formatting
print("          ~~A Lovely Story of a Millennial~~")
print()
print()

# Print the opening and background of the story
print("You are a millennial in twenty-first century and you are trying to make it into society. You embark on a soul searching hike to contemplate your future efforts towards success and happiness.")
print()

# Prompt the user to select from three different professional career paths and print them as multiple choice items
print("Your thoughts take you to your future livelihood and main aim of your next few years. You will choose from the following endeavors:")
print("a. Learn to become an dance artist")
print("b. Become an engineer")
print("c. Live life spontaneously as a vagabond")

# Store the response as a variable
lifePath = input("What do you pick from the following three paths? Enter a, b, or, c: ")
print()


# Create a story branch based on the selection of the user from the multiple choice 
# If the user selects option "a" then start this branch of code
if lifePath == "a":
  print("For a successful dance artist you have to learn many different style of dance techniques. It is important to physically practice and learn from professionals. You decide to become an artist but you are not sure what is the most efficient path to becoming one.")
  print()
  print("You get the following three advises from fellow hikers:")
  print("a. Get a job at Walmart and in your breaks practice freestyle dancing in the parking lot.")
  print("b. Buy a motorcycle on your credit card and learn to dance on a speeding bike, Evel Knievel style.")
  print("c. Apply for an admission in an art school, there happens to be an excellent one in your home town with dance major.")
  dance = input("What advise do you take? Enter a, b, or c: ")
  print()

  
  if dance == "a":
    print("You were practicing to dance in the Walmart parking lot and got hit by an SUV of a speeding Black Friday shopper.")
  elif dance == "b":
    print("One evening you were dancing standing on the seat of your motorcycle speeding 100mph on interstate 95 and you ran into a deer.")
  elif dance == "c":
    print("You miraculously were accepted into the art school with full scholarship and you are on your way to a happy fulfilling life of dance and movements.")
  else:
    print("That is not a valid response.")


# If the user selects option "b" then start this branch of code
elif lifePath == "b":
  engineer = input("How do you spell Engenier?: ")
  if engineer == "engineer" or engineer == "Engineer":
    print("Your don't have the mental aptitude to be an engineer.")
  else:  
    print("Your can't seem to spell. You must be good at math, you will be successful and have a happy life as an engineer.")


# If the user selects option "c" then start this branch of code
elif lifePath == "c":
  print("Being a vagabond is a challenging road, but you will be happy living the life you choose rather than living the life of responsibility or corporate slavery. Now is the time to make this happen. You remember your parents advise to get married and have kids quickly so they can play with their grandkids. Should you take this advise?")
  vagabond = input('Enter "yes" or "no": ')
  print()

  
  if vagabond == "yes" or vagabond == "Yes":
    print("Your go through your arranged marriage and have many lovely kids. You are forced to take a full-time job to support your family. You end up living an unhappy life of corporate slavery.")
  elif vagabond == "no" or vagabond == "No":
    print(" With this choice you have a better chance of living your dreams and being happy.")
  else:
    print("That is not a valid response.")
  
    
else:
  print("That is not a valid response. ")

# This will print regardless of the the path chosen 
print("The End.")