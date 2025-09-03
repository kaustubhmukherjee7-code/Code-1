import os

# specify the directory path
directory_path = 'E:\\'

# use os.listdir() to get contents
contents = os.listdir(directory_path) #To get all contents 
a = os.path.exists(directory_path) # To check if the path exists or not(True/False)
# print each item
for item in contents:
    print(item)
print("Check if it exists or not:-")
print(a)


