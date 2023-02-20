from tkinter import END
import os


def read_patches_from_file(path_type, file_type: str) -> tuple:
    """

    Reading no more than 5 last used paths from txt file which store this info

    """
    # Checking if files is exists
    if not os.path.exists(file_type):
        with open(file_type, "w", -1, 'utf-8') as f:
            pass

    with open(file_type, 'r', -1, 'utf-8') as f:
        values = []
        for i in f:
            value = i.strip()
            values.append(value)
        path_type.delete(0, END)

        if values:
            last_value = values[0].strip()
            path_type.insert(0, last_value)

    return tuple(values)


def write_patches_to_file(path: str, values: tuple, file_type: str):
    """

    Writing last 5 folder's paths to combobox menu next to "Select" button

    """
    if values:
        tuple_list = list(values)
        if path.strip() != tuple_list[0].strip():

            if path.strip() in tuple_list:
                path = path.strip()
                tuple_list.remove(path)

            if len(tuple_list) >= 5:
                tuple_list.pop(-1)

            with open(file_type, 'w', -1, 'utf-8') as f:
                f.write(path.strip() + '\n')
                for i in tuple_list:
                    f.write(i.strip() + '\n')

    else:
        with open(file_type, 'w', -1, 'utf-8') as f:
            f.write(path.strip())


def make_copy_dir(path_to_destination: str):
    """
    Make destination directory if this is not exists
    """
    if not os.path.exists(path_to_destination):
        path_split = path_to_destination.split('/')
        path_process = ''
        for i in path_split:
            path_process += i + os.sep
            if os.path.exists(path_process):
                continue
            else:
                os.mkdir(path_process)
