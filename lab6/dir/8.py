import os


def delete_file(file_path):
    try:
        if os.access(file_path, os.F_OK):
            print(f"File at {file_path} exists.")

            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File at {file_path} successfully deleted.")
            else:
                print(f"No write access to the file at {file_path}.")
        else:
            print(f"File at {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_to_delete = 'example.txt'
delete_file(file_to_delete)
