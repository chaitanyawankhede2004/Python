def mystery(l):
    if l == []:
        return(l)
    else:
        return(l[-1:]+mystery(l[:-1]))
        
print(mystery([23,35,19,58,93,46])) 
pairs = [ (x,y) for x in range(6,1,-1) for y in range(3,1,-1) if (x+y)%2 == 0 ]
print([ (x,y) for x in range(6,1,-1) for y in range(3,1,-1) if (x+y)%2 == 0 ])
print(pairs)
goals = {"Country":{"Ronaldo":123,"Messi":103,"Pele":83},"Club":{"Ronaldo":[512,51,158],"Pele":[604,49,26]}}
#goals["Club"]["Messi"][0:] = [496,71,145]
#goals["Club"]["Messi"].extend([496,71,145])
goals["Club"]["Messi"] = [496,71,145]
#goals["Club"]["Messi"] = goals["Club"]["Messi"] + [496,71,145] 

wickets={}
wickets["Muralitharan, tests"] = 800
wickets["Muralitharan"] = {"tests":800}
wickets[("Muralitharan","tests")] = 800
#wickets[["Muralitharan","tests"]] = 800 
