#classes in python are defined using the class keyword and is collection of mehods
class calc:
    answer = 0;
    def add(x,y):
        answer = x+y
        return answer
    def sub(x,y):
        answer = x-y
        return answer
    def mult(x,y):
        answer = x*y
        return answer
    def div(x,y):
        answer = x/y
        return answer

print(calc.add(2,5))
print(calc.sub(2,5))
print(calc.mult(2,5))
print(calc.div(2,5))
