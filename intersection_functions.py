# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------
#     Given two rules in the following format                                    ------

#     R1 = ( (1, 2, 3, 8, 11), (4, 6), 'A')                                      ------
#     R2 = ( (9,12),            5,     'C')                                      ------

#     The function " intersection " returns                                      ------
#     True if the rules intersect each other and                                 ------
#     False if they do not intersect                                             ------

#     Two rules INTERSECT each other IF the intervals formed with the minimum and  ----
#     maximum values of the sets located AT EACH parameter i intersect each other  ----
#     i.e INTERSECTION == True if ALL parameters intersect
#--------------------------------------------------------------------------------------

#Given a tuple, integer or float returns the maximum and minimum values
def interval(element):
    if type(element)==int:
        minimum = element
        maximum = element
    elif type(element)==float:
        minimum = element
        maximum = element
    else:
        minimum = min(element)
        maximum = max(element)
    #print('min,max',minimum,maximum)
    return (minimum,maximum)

#interval(7)
#min_max((1,3,6))

#Check if two intervals, defined by its minimum and maximum values,
#intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
#interval_intersection( (1,11), (9,12) )
#interval_intersection( (2,5), (1,11) )
        
# NOTE that this function returns the INTERSECTION DISREGARDING THE CLASS
        
#Given two rules Returns true if they intersect each other
def intersection(rule1, rule2):
    intersection = True
    for i in range( len(rule1) - 1 ):
        if interval_intersection( interval(rule1[i]), interval(rule2[i]) ) == False:
            intersection = False
    return intersection
"""
tests

Example 1:
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')

intersection( ( (2,5),             7,     'D'), ( (1, 2, 3, 8, 11), (4, 6), 'A') )
intersection ( (5, 4,'B'), ( (1, 2, 3, 8, 11), (4, 6), 'A'))
intersection( ( (1, 2, 3, 8, 11), (4, 6), 'A'), ( (9,12),            5,     'C'), )
intersection((     5,             4,     'B'),( (2,5),             7,     'D'))
intersection(( (9,12),            5,     'C'),(     5,             4,     'B'),)

Example2:
intersection(  ( (9, 12), 5, 'C'),( (10, 10.5 ), 4, 'B') )
intersection(  ( (9, 12), 5, 'C'),( (10, 10.5 ), 5, 'B') )

Example3:
intersection(((1,4),3,'A'), (2,(1,4),'A'))
intersection(((1, 4), 3, 'A'), (4, (3, 6), 'A'))

"""
#--------------------------------------------------------------------------------------------
#    Intersection: All parameters of the new instance intersect the intervals formed by
#    the (min and max) values of an existing rule.
#
#    Possible rule formation: The new instance would have formed a rule with another instance.
#---------------------------------------------------------------------------------------------
def intersection_or_possible_rule_formation( new_pattern, rule, risk ):
    # INTERSECTION WITH SOME RULE
    intersection = True
    for i in range( len(rule) - 1 ):
        if interval_intersection( interval(new_pattern[i]), interval(rule[i]) ) == False:
            intersection = False
    # POSSIBLE RULE FORMATION WITH RULEX i.e new_pattern and rule differ <= risk having same class
    possible_rule_formation = False
    lenght = len(rule) -1
    if new_pattern[-1] == rule[-1]:
        different_parameters = 0
        for i in range( len(rule) -1 ):
            if new_pattern[i] != rule[i]:
                different_parameters += 1
        if different_parameters <= risk:
            possible_rule_formation = True
    # Return True if either new_patterns intersects a rule or
    # if it would have created a rule (by calling rulex) with another single instance or rule
    if intersection == True or possible_rule_formation == True:
        return True
    else:
        return False

#      Test to see if this really works
#res = intersection_or_possible_rule_formation([1, 2, 'A'], [2,2,'A'], 1)
#res = intersection_or_possible_rule_formation( [ 1, 2, 'A'], [2, 2, 'B'], 1)
#print(res)
