# This is the main file of the build where we will pull all the functions in.
import character_name
import character_class
import character_origin
import character_stats

def main():

    print("This is my Dungeons and Dragons character creator program.  It is a first version.")

    input("Welcome to Sean's Python based Dungeons and Dragons Character creator!  Press Enter to continue!")

    character_name.name()

    input("Press Enter to choose your class!")

    character_class.class_type()

    input("Now it is time to select your characters origin.  Press enter to see the options:")

    character_origin.class_origin()

    input("Up next are your character stats.  This is the fun part! Press Enter to continue!")

    character_stats.dice_rolls()
    character_sheet = open('charactersheeet.txt', 'w')
    data_1 = open('charactername.txt')
    data_1_import = data_1.read()
    data_2 = open('class.txt')
    data_2_import = data_2.read()
    data_3 = open('origin.txt')
    data_3_import = data_3.read()
    data_4= open('stats.txt')
    data_4_import = data_4.read()
    data_print = str(data_1 + data_2 + data_3 + data_4)
    character_sheet.write(data_print)
    print("You have finished your character creation.  You will now have a charactersheet.txt file to reference all your information!")

main()