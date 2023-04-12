"""File I/O Operations"""


def write(text):
    """Write text to file(Overwrites)"""
    with open("data.csv", mode="w") as data:
        data.write(text)


def append(text):
    """Append text to file"""
    with open("data.csv", mode="a") as data:
        data.write(text + "\n")
