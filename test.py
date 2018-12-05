#-------------------------------------------------------------------------------
#                                               --------------------------------
#                     test                      --------------------------------
#                                               --------------------------------
#                                               --------------------------------
#                                               --------------------------------
#                                               --------------------------------
#-------------------------------------------------------------------------------

import sys
from intersection_functions import sameClass
from intersection_functions import interval

def test(l):
    l()
    sys.stdout.write('.')

def xxx():
    rule1 = (1,2,'A')
    rule2 = (1,2,'B')
    assert sameClass(rule1,rule2)==False
    rule1 = [{1},{2},'A']
    rule2 = [{1},{2,4},'A']
    assert sameClass(rule1,rule2)==True
test(xxx)    

def xxx():
    assert interval(7) == (7,7)
    assert interval((1,3,7)) == (1,7)
    assert interval([1,5,7]) == (1,7)
    assert interval({1})==(1,1)
    assert interval( {5,7,11} ) == (5,11)
test(xxx)

print('\n All passed!')
