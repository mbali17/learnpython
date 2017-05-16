'''
In the below function the order of the parameters does not matter but if
there is a function accepting different types of parameters then the order
matters refer the second function for example.
'''
def addition(num1,num2):
    answer = num1+num2
    return answer

sumOfTwoNumbers = addition(33,44)
print(sumOfTwoNumbers)
#function parameters can also be given the default values
def website(font='arial',bg_color='red',font_color='grey',font_size=14):
    print('font:',font)
    print('background color:',bg_color)
    print('font color:',font_color)
    print('font_size:',font_size)
#invoking the function with correct parameters.
website('TNR','white','black',11)

#invoking the function by changing the order of the parameters.
website('white','TNR','black',11)
'''
invoking the funcion by passing lesser parameters
This invokation would through an exception but if it is exceuted with default
values assigned to the paramters this would not through any exception as it
uses the default value.
'''
website('white','black',11)

#invoking the function using the actual parameter name.
website(bg_color='white',
        font='TNR',
        font_color='black',
        font_size=11)
#invoking functions with only the parameters needed to be modified.
website(bg_color='white',
        font_color='black')
#invoking the function with default params
website()
