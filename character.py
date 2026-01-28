#This is the start of the program for now it will do the following
# Ast you to input a first name and last name, then it will print that name.
# After that it will give you the preset stats or tell you where to go to roll 4d6 and drop the lowest one so you can assign stats
# All character stats will be variables they may get moodified later
# Also you will get to select your class and origin which will tell you which status you may want to focus on
# We will also add versioning listing to explain when a new feature may get added



print("Welcome to the Character Creator v0.1")
# Request the player to give their character a name.
first_name = input("Please enter your character's first name: ")
last_name = input("Please enter your character's last name: ")
print(f"Your character's name is {first_name} {last_name}.")


#Let the player choose a class.
print("Next select your character class from the following options: Barbarian, Wizard, Paladin")
class_choice = input("Please enter the name of your chosen class: ")
class_choice = class_choice.lower()
if class_choice == "barbarian":
    print("You have chosen Barbarian! Focus on Strength and Constitution.")
elif class_choice == "wizard":
    print("You have chosen Wizard! Focus on Intelligence and Wisdom.")
elif class_choice == "paladin":
    print("You have chosen Paladin! Focus on Strength and Charisma.")
else:
    print("Invalid class choice. Please restart the program and choose a valid class.")
print("Now it is time to select your characters origin from the following options: Acolyte, Criminal, Sage, Soldier")

#Origins are something new to me as far as DnD goes so I've added them but they don't seem to do much yet.
origin_choice = input("Please enter the name of your chosen origin: ")
origin_choice = origin_choice.lower()
if origin_choice == "acolyte":
    print("You have chosen Acolyte! Focus on Wisdom and Charisma.")
elif origin_choice == "criminal":
    print("You have chosen Criminal! Focus on Dexterity and Intelligence.")
elif origin_choice == "sage":
    print("You have chosen Sage! Focus on Intelligence and Wisdom.")
elif origin_choice == "soldier":
    print("You have chosen Soldier! Focus on Strength and Constitution.")
else:
    print("Invalid origin choice. Please restart the program and choose a valid origin.")

#Start adding stat info.
print("Now it's time to assign your character's stats.")
print("You can either use the preset stats or roll 4d6 and drop the lowest die.")
stat_choice = input("Type 'preset' to use preset stats or 'roll' to roll for stats: ")
stat_choice = stat_choice.lower()
if stat_choice == "preset":
    print("Where would you like to assign the following preset stat numbers? 15, 14, 13, 12, 10, 8")
    stat_15 = input("Please enter the stat you want for the 15 in the format 'Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma': ")
    stat_14 = input("Please enter the stat you want for the 14: ")
    stat_13 = input("Please enter the stat you want for the 13: ")
    stat_12 = input("Please enter the stat you want for the 12: ")
    stat_10 = input("Please enter the stat you want for the 10: ")
    stat_8 = input("Please enter the stat you want for the 8: ")
    print(f"Preset stats assigned.  Your stats are as Follows: {stat_15} = 15, {stat_14} = 14, {stat_13} = 13, {stat_12} = 12, {stat_10} = 10, {stat_8} = 8")
elif stat_choice == "roll":
    print("To roll for stats, please visit an online dice roller that supports rolling 4d6 and dropping the lowest die.  For example goto google.com and search for d6 roller, or use your own dice!")
    print("After rolling, assign the resulting numbers to your character's stats.")
else:
    print("Invalid choice. Please restart the program and choose either 'preset' or 'roll'.")

print("Thank you for using the Character Creator v0.1! Your character creation is now complete.")   
print(f"Character Summary:\nName: {first_name} {last_name}\nClass: {class_choice.title()}\nOrigin: {origin_choice.title()}")
print(f"Character stats have been assigned based on your choice of '{stat_choice}'.")

# End of character.py