import os


def read_file(filename):

    try:

        with open(filename, "r", encoding="utf-8") as file:

            return file.read()

    except FileNotFoundError:

        return f"File Error: '{filename}' was not found."

    except Exception as error:

        return f"File Error: {error}"


def write_file(filename, content):

    try:

        with open(filename, "w", encoding="utf-8") as file:

            file.write(content)

        return f"File '{filename}' written successfully."

    except Exception as error:

        return f"File Error: {error}"