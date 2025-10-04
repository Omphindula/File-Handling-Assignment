def read_and_write_file():
    try:
        input_file = input("Enter the name of the file to read: ")
        with open(input_file, "r") as file:
            content = file.read()
        modified_content = content.upper()
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)
        print(f"Modified content has been written to '{output_file}' successfully.")
    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
