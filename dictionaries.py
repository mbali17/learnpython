'''
Dictionaries are a datatype in python which are based on key value pairs.
Keys are always unique while the values can have duplicates.The type of key
can be anything but is either string,int or float. The values can be either
function,list,string,float etc
'''
gradDict={"Jane":45,"Dave":34,"kary":34,"sumo":56}
print(gradDict);
#update the value of dave
gradDict["Dave"]=76
print(gradDict)
#print the value obtained by sumo
print(gradDict["sumo"])
#The value can be list as well.
gradDict={"Jane":[45,54],"Dave":[34,43],"kary":[35,53],"sumo":[56,65]}
print(gradDict)
#obtain the marks scored by jane in first test
print(gradDict["Jane"][0])
