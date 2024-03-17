from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin


def main():
    user_input = input_from_console()
    output_to_console("Text from console input: " + user_input)
    write_to_file_builtin("data/input_text.txt", user_input)
    file_content = read_from_file_builtin("data/input_text.txt")
    output_to_console("Text read from file using built-in functions: " + file_content)


if __name__ == "__main__":
    main()
