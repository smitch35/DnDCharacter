# This is where we will collect information about the player as a function

def name():
    first_name = input("Please Enter your characters first name: ")
    last_name = input("Please Enter your characters last name: ")

    name_file = open('charactername.txt','w')

    name_file.write(f'{first_name}\n')
    name_file.write(f'{last_name}\n')

    name_file.close()

if __name__ == '__main__':
    name()