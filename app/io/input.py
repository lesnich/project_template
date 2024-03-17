def input_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text input by the user.
    """
    return input("Enter text: ")


def read_from_file_builtin(filename):
    """
    Function to read from a file using Python's built-in capabilities.

    Parameters:
        filename (str): The name of the file to read from.

    Returns:
        str: The content read from the file.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_from_file_pandas(filename):
    """
    Function to read from a file using the pandas library.

    Parameters:
        filename (str): The name of the file to read from.

    Returns:
        pandas.DataFrame: The data read from the file as a DataFrame.
    """
    import pandas as pd
    return pd.read_csv(filename)

# Additional functions or code can be added below
