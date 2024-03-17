

def output_to_console(text):
    """
    Function to output text to the console.

    Parameters:
        text (str): The text to be printed to the console.
    """
    print(text)


def write_to_file_builtin(filename, content):
    """
    Function to write to a file using Python's built-in capabilities.

    Parameters:
        filename (str): The name of the file to write to.
        content (str): The content to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)
