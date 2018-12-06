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
from intersection_functions import interval_intersection
from intersection_functions import intersection
from adjacent_matrix import adjacent_matrix

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

def xxx():
    assert interval_intersection( (1,11),(9,12) ) ==True
    assert interval_intersection( (2,5), (1,11) ) ==True
    assert interval_intersection( (2,5), (5,7) ) == True
    assert interval_intersection((1,1),(2,2)) == False
test(xxx)

def xxx():
    #Example 1:
    #( (1, 2, 3, 8, 11), (4, 6), 'A'),
    #( (9,12),            5,     'C'),
    #(     5,             4,     'B'),
    #( (2,5),             7,     'D')

    assert intersection( ( (2,5), 7, 'D'), ( (1, 2, 3, 8, 11), (4, 6), 'A') ) == False
    assert intersection ( (5, 4,'B'), ( (1, 2, 3, 8, 11), (4, 6), 'A')) == True
    assert intersection( ( (1, 2, 3, 8, 11), (4, 6), 'A'), ( (9,12), 5, 'C'), ) == True
    assert intersection(( 5, 4, 'B'),( (2,5), 7, 'D')) == False
    assert intersection(( (9,12),  5,  'C'),( 5,   4,  'B'),) == False
test(xxx)

def xxx():
    R = [
            ( (1, 2, 3, 8, 11), (4, 6), 'A'),
            ( (9,12),            5,     'C'),
            (     5,             4,     'B'),
            ( (2,5),             7,     'D')
            ]
    assert adjacent_matrix(R) == {'0': ['1', '2'], '1': ['0'], '2': ['0'], '3': []}
test(xxx)



print('\n All passed!')












