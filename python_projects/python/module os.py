import os
if not os.path.exists("hello"):
    os.mkdir("hello")#makes a directory
#for i in range(100):
   # os.mkdir(f"hello/codes{i}")
print(os.getcwd())
os.chdir("\users")#to change the directory
print(os.getcwd())
#folders = os.listdir("hello")
#print(folders)
#for folder in folders:
    #print(folder)
