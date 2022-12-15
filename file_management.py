"""
Read from files of different file types.
"""


def read_file(filepath):
    try:
        with open(filepath) as file_object:
            file_object.read()
    except FileNotFoundError:
        print("File not found.")

    with open(filepath) as file_object:
        return file_object.read()


def main():
    print(read_file('./txt_files/dressing_room.txt'))


if __name__ == '__main__':
    main()
