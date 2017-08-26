'''
To accept value from the user we use the input metho.
'''
name = input("What is your name: ")
print("Hello",name)
#Statistics is a module used to find mean,median,mode,standard deviation for a
#given list.
import statistics
exList = [1,2,4,6,7,2,3,67,8,22]
x = statistics.mean(exList)
print("mean",x)
x = statistics.median(exList)
print("median",x)
x = statistics.mode(exList)
print("mode",x)
x = statistics.stdev(exList)
print("standard deviation",x)
