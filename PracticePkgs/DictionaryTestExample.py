'''
Created on 24 Jun 2025

@author: User
'''


dictVariable={"test":1,"test2":2,"test3":3}

for a in dictVariable.keys():
    print("values ="+str(dictVariable[a]))
    
    
tuple_example=(dictVariable,"a","b","c","d")

for v in tuple_example:
    if(type(v)==dict):
        print("Displaying key values "+str(v.keys()))
    else:
        print("Tuple example  ="+str(v))
        
print(tuple_example.count(0))