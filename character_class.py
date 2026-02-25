def class_type():
    class_choice = input("Please enter the name of your chosen class (Choices are Barbarian, Wizard, Paladin.): ")
    class_choice = class_choice.lower()
    if class_choice == "barbarian":
        print("You have chosen Barbarian! Focus on Strength and Constitution.")
    elif class_choice == "wizard":
        print("You have chosen Wizard! Focus on Intelligence and Wisdom.")
    elif class_choice == "paladin":
        print("You have chosen Paladin! Focus on Strength and Charisma.")
    else:
        print("Invalid class choice. Please restart the program and choose a valid class.")