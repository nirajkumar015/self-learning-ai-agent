import os


# Keep all agent-created files inside this folder.
BASE_DIR = os.path.abspath("agent_files")

os.makedirs(BASE_DIR, exist_ok=True)


def safe_path(filename):

    # Remove accidental surrounding spaces
    filename = filename.strip()

    # Don't allow empty filenames
    if not filename:
        raise ValueError("Filename cannot be empty.")

    # Convert filename into an absolute path inside BASE_DIR
    full_path = os.path.abspath(
        os.path.join(BASE_DIR, filename)
    )

    # Make sure the final path stays inside BASE_DIR
    if os.path.commonpath([BASE_DIR, full_path]) != BASE_DIR:
        raise ValueError(
            "Access outside the agent_files folder is not allowed."
        )

    return full_path


def read_file(filename):

    try:

        path = safe_path(filename)

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except FileNotFoundError:

        return f"File Error: '{filename}' was not found."

    except Exception as error:

        return f"File Error: {error}"


def write_file(filename, content):

    try:

        path = safe_path(filename)

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return (
            f"File '{filename}' written successfully."
        )

    except Exception as error:

        return f"File Error: {error}"