'''
import is used to include function from a library.
1)we can import the complete statistics module using
import statistics -- with this we would have to type the word statistics every
time the methods are to be invoked.
2)we can as well alias the library using the as keyword
import statistics as s
so when invoking the method we would use s.methodname rather than statistics.methodName
3)we can import specific method and alias them as well
from statistics import mean as m ,stdev as s
when invoking we can just use s(exList) or m(exList)
4)we can import the complete library and avoid typing the library name as well
from statistics import *
'''
exList = [1,2,4,6,7,2,3,67,8,22]

#import statistics
#print(statistics.mean(exList))

import statistics as s
print(s.mean(exList))

from statistics import stdev as sdev
print("Standard deviation",sdev(exList))

from statistics import *
print("mode:",mode(exList))
