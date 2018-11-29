import pymodule
pymodule.sayhi()
print("name : ",pymodule.__name__)
print("version : ",pymodule.__version__)
print("doc : ", __doc__)
print("file : ", __file__)
print("package : ", __package__)
print("spec : ", __spec__)


# To import everything from a Module, use =======================================================

from pymodule import *

pymodule.sayhi()


# Above doesn't work ==========================

#import  this


# The dir function ==============================

# run as command on command line


