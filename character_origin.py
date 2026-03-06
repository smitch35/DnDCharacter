def class_origin():
    print("Now it is time to select your characters origin from the following options: Acolyte, Criminal, Sage, Soldier")
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

    origin_file = open('origin.txt', 'w')
    origin_file.write(f'This is your background origin: {origin_choice}.  Use this to help design your character story!\n')

if __name__ == '__main__':
    class_origin()