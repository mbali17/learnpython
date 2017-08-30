'''
modules in pyhon are just a separate script with functions defined in it.
To import an module, it has to be present in one of the following places
    1)in the same directory as your script.
    2)In the lib folder of the python installation directory(i,e: where the
    python is installed.)
    3)In the lib/site-packages where the third party libraries are present. In
    order to add a new module we can copy the source and place it in the
    lib/site-packages folder.
in order for this program to work copy the example module to the
lib/site-packages folder.
We can as well create virtual environment which is like a workspace for the project. and we could use the 
python from the virtualenveironment and the python would perform the same check but,in the virtual environment 
'''
import examplemodule
examplemodule.sampleFunction("This is the data to be printed.")
