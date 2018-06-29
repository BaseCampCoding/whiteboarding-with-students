def name_file(file_name):
    with open(file_name) as file:
        file.readline()  # to skip the first line
        contents = file.read()
    student_list = contents.split('\n')
    return student_list


def list_to_dictionary(names):
    dictionary = {}
    for name in names:
        dictionary[name] = False
    return dictionary


def main():
    pass


if __name__ == '__main__':
    main()