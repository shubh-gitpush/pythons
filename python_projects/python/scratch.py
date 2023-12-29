#dictionary
dict={'india':"delhi","spain":"barclelona","germany":"berlin"}
print(dict["spain"])
for key,values in dict.items():
    print(key,":",values)#line by line
print(dict.keys())
print(dict.values())
dict.pop("spain")#removes item
print(dict)
dict.popitem()#for last item
yo={1: {"eminem":"lose yourself","tupac":"only god can judge me"},
    2:{"dr dre":"still dre","ice cube":"no vaseline","eazy-e":"real m gs"}}
print(yo)