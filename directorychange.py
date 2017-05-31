from contextlib import contextmanager
import os

@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    print("path changed")
    try:
        yield
    finally:
        os.chdir(current_dir)
#the with key word allows us to write code which needs releasing of resources and
# with 'with' keyword once the context is left the resources are releases
with working_directory("C:\ALI"):
    # do something within data/stuff
    open('sometext.txt','r')
# here I am back again in the original working directory
print(os.getcwd)
open('somefile.txt','w')