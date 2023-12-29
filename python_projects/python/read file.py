a=open("read.txt.html",'r')
i=0
while True:
    i=i+1
    line=a.readline()#reads the file line by line
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"the marks of student{i} in sst:{m1} ")
    print(f"the marks of student{i} in sci:{m2} ")
    print(f"the marks of student{i} in eng:{m3} ")
b="26,3224,55434"
print(b.split(",")[0])