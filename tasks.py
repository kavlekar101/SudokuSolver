from invoke import task
from ctypes import *

@task
def build(c, string):
    lib = CDLL("libtrial.so")
    lib.printString(len(string), c_char_p(string))

