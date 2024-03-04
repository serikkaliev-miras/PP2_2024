import os
def check(path):
	if os.path.exists(path):
		print(f"the way {path} exist")
 	else:
		print(f"the way {path} not exist")
		return 
    if os.access(path , os.R_OK):
        print(f"path {path} available for reading")
    else:
        print(f"path {path} not available for reading")
    if os.access(path , os.W_OK):
        print(f"path {path} writability")
    else:
        print(f"path {path} not writability")
    if os.access(path , os.X_OK):
        print(f"path {path} executability")
    else:
        print(f"path {path} not executability")
path = "/path/to/your/directory_or_file"
check(path)
