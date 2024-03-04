import string

def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f"{letter}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is the content of file {file_name}")
            print(f"The fail {file_name} generated completely.")

generate_text_files()
