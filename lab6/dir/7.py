def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

        print(f"The contents of the file were successfully copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"An error has occurred: {e}")
-
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'
copy_file(source_file_path, destination_file_path)
