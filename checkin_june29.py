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


def valid_names(students):
    '''Dict -> Set
    >>> valid_names({'lisa': False, 'oz': False, 'trey': False})
    {'lisa', 'oz', 'trey'}
    '''
    return set(students.keys())


def string_names(student_dict):
    '''
    >>> string_names({'a': ..., 'b': ..., 'c': ...})
    a, b, c
    '''
    print(', '.join(student_dict))


def input_valid_name(valid_names):
    while True:
        user_response = input('Name: ')
        if user_response in valid_names:
            return user_response
        else:
            print('Please provide a valid name')


def main():
    pass


if __name__ == '__main__':
    main()