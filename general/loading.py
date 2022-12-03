def open_data_file(path):
    with open(path) as file:
        rawinput = file.read().splitlines()
    return rawinput