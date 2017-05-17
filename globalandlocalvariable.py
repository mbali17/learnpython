'''
This is a global variable. this can be acessed in any method but,
cannot be modified. If this need to be modified and the modified value
is required to be used further then there are two ways to do it
    1) using the global keyword which allows the variable to be modified
    and the modified value can be accessed in the other part of the program.
    2)creating temporary variables and assigning the returned value from the
    modified function. this is among the best practices.
'''
x=6;
def example():
    z=5;
    print(z)
def example2():
    z=8
    #this line would throw an exception 
    #x+=1
    #Hence to achieve this following can be done
    y=x+1;
    print(z)
    print(y)
    return y

#now to get the modified value capture the return form example2 and this is
#the best practice.
x=example2()
print(x)

def example3():
    global x;
    x+=1;
    print(x)

print(x)
