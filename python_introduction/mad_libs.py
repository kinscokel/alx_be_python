# Mad Libs story with conditional statement

# Ask the user for adjectives
adj1 = input("Enter an adjective to describe the day): ")
adj2 = input("Enter another adjective to describe the monkey): ")
adj3 = input("Enter a third adjective to describe the lion) :")
adj4 = input("Enter one last adjective to describe the experience): ")
animal = input("Enter an animal you 'd be surprise to see at the zoo: ")
feeling = input("How did you feel after the visit? ")

# construct a story template with placeholders for the user provided words using "f-strings"

story = f'''On a beautiful {adj1} day, I went to the zoo. 
 I saw a funny {adj2} monkey swinging from the tress.
 Then, I spotted a majestic {adj3} lion lounging in the sun.
 What a wild and {adj4} experience!
 By the end of the day i was {feeling}!'''

# Use of conditional satement
if adj1 == "Cloudy":
  
    print("Despite the dull weather, the animals were still lively")
else:
    print("The air made it refreshening")

if animal == "Unicorn":
    print("I couldn't believe my eyes when i saw a {animal}, i never expected!")   

else:
    print("There was even a {animal}, I did'nt expect!")

print(story)    
    



   
     




     

