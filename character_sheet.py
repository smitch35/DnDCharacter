def character_sheet():

    file_paths = ['charactername.txt', 'class.txt', 'origin.txt', 'stats.txt']

    with open('chracter_sheet.txt', 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as input_file:
                for line in input_file:
                    output_file.write(line)


if __name__ == '__main__':
    character_sheet()
