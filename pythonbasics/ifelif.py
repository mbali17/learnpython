x=3
y=7
z=18
'''
If there are 2 conditions in the elif stack that satisfy the condition then
the first block satisfying the condition is only executed, If you would have
to check multiple conditions then we would have to use the if statement.
'''
if x > y and x < z:
    print(x,'is greate than',y,'and x is less than',z)
# The following elif statements both are true but only
#the first block is executed.
elif z>y:
    print(z,'is greater than',y)
elif y>x:
    print(y,'is greater than',x)
else:
    print('none of the conditions are satisfied')
