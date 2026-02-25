# This is the main file of the build where we will pull all the functions in.
import character_name
import character_class
import character_origin
import character_stats

def main():

    input("Welcome to Sean's Python based Dungeons and Dragons Character creator!  Press Enter to continue!")

    character_name.name()

    input("Press Enter to choose your class!")

    character_class.class_type()

    input("Now it is time to select your characters origin.  Press enter to see the options:")

    character_origin.class_origin()

    input("Up next are your character stats.  This is the fun part! Press Enter to continue!")

    character_stats.dice_rolls()

main()