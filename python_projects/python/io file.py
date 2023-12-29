#f=open("notebook.txt.html")#helps to open a file
#print(f)
#text = f.read()#helps to read
#print(text)

f=open("notebook.txt.html","w")#helps to open a file
print(f)
text = f.write("hello")#helps to write"w"
print(text)
f.close()