questions=[["how many seats are there in lok sabha as of 2023?","a.450","b.543","c.540","d.348"],
["which language was used to make this proram","a.c++","b.python","c.html","d.C"],
["in which demonitization occured?","a.2015","b.2016","c.2020","d.2022"],
["who acquired the big bazaar retail chain recently?","a.tata","b.reliance","c.aditya birla group","d.wipro"],
["who is the current i.t minsiter of indian","a.nirmila sitaraman","b.vishnaw manshaw","c.amit shah","d.mansukh"],
["which loop was used to make this program","a.while loop","b.for loop","c.def function","d.none of the above"],
["who is the 16h president of india?","a.ramnath govind","b.drapaudi murmu","c.a.p.j abdul kalam","d.dr.rajendra prasad"],
["in which engine fortnite was built on?","a.unity","b.unreal","c.panda 3D","d.game engine 3"]]
levels=[1000,2000,4000,8000,16000,32000,64000,128000]
money=0
for i in range(0,len(questions)) :
     question=questions[i]
     print(f"{question[0]}")
     print(f"question for rs{levels[i]} ")
     print(f"{question[1]}          {question[2]}"  )
     print(f"{question[3]}          {question[4]}")
     answer=str(input("the answer"))
     if answer==question[2]:
        print(f"the answer is correct,you have won rs {levels[i]}")
        if i==4:
            money=8000
        elif i==8:
            money=128000
     else:
        print("you have lost")
        break;
print(f"{money} you have won")