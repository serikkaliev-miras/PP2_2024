import os
def c(pathh):
    if os.path.exists(pathh):
        print(f"path {pathh} exists")
    	dirname , filename = os.path.split(pathh)
    	print(f"filename : {filename}")
    	print(f"dirname : {dirname}")
	else:
    print(f"path {pathh} not exists.")
input = input("")
c(input)