from os import walk

#inp=input("Enter the directory:")
dir_path = r'C:\Users\abhir\work\training'

res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
for i in range(0,len(res)):
    print(res[i])