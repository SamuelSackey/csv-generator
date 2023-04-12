"""File I/O Operations"""


def write(text):
    """Write text to file(Overwrites)"""
    try:
        with open("data.csv", mode="w") as data:
            data.write(text)
    except Exception as e:
        print("An error occurred while writing to the file.", e)


def append(text):
    """Append text to file"""
    try:
        with open("data.csv", mode="a") as data:
            data.write(text + "\n")
    except Exception as e:
        print("An error occurred while writing to the file.", e)
