def name_file(file_name):
    with open(file_name) as file:
        file.readline()  # to skip the first line
        contents = file.read()
    student_list = contents.split('\n')
    return student_list


def main():
    pass


if __name__ == '__main__':
    main()