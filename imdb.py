import json
data=json.load(open("imdb.json"))
list=[]
for i in range(len(data)):
    #print(type(data[i]))
    #cprint(data[i]["genre"])
    if "Action" in data[i]["genre"]:
        if(data[i]["imdb_score"]==8.8):
            list.append(i)
           
for i in list:
    print("Director:"+data[i]["director"])
    print("Movie:"+data[i]["name"])
    print("\n")
                  
        