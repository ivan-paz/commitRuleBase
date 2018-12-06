# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------
#                                                                                ------
#                                                                                ------
#     Given two rules in the following format                                    ------
#                                                                                ------
#                                                                                ------
#     R1 = ( (1, 2, 3, 8, 11), (4, 6), 'A')                                      ------
#     R2 = ( (9,12),            5,     'C')                                      ------
#                                                                                ------
#     The function " intersection " returns                                      ------
#     True if the rules intersect each other and                                 ------
#     False if they do not intersect                                             ------
#                                                                                ------
#     Two rules INTERSECT each other IF the intervals formed with the minimum and  ----
#     maximum values of the sets located AT EACH parameter i intersect each other  ----
#     i.e INTERSECTION == True if ALL parameters intersect                       ------
#                                                                                ------
#                                                                                ------
#                                                                                ------
#--------------------------------------------------------------------------------------


# Given two rules returns False if they DO NOT have the same class and True otherwise
def sameClass(rule1, rule2):
    if rule1[-1] != rule2[-1]:
        return False
    return True

#Given a tuple, integer or float returns the maximum and minimum values
def interval(element):
    #if type(element) == list:
    #    print(' element  ', element)
    if type(element)==int:
        minimum = element
        maximum = element
    elif type(element)==float:
        minimum = element
        maximum = element
    else:
        minimum = min(element)
        maximum = max(element)
    return (minimum,maximum)

#Check if two intervals, defined by its minimum and maximum values intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
        
# NOTE that this function returns the INTERSECTION DISREGARDING THE CLASS 
#Given two rules Returns true if they intersect each other
def intersection(rule1, rule2):
    intersection = True
    for i in range( len(rule1) - 1 ):
        if interval_intersection( interval(rule1[i]), interval(rule2[i]) ) == False:
            intersection = False
    return intersection



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
            if new_pattern[i] != rule[i] and is_contained(new_pattern[i],rule[i]) == False: #And it is NOT contained
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

#    See if every element of pattern[i] is in rule[i]
#
def is_contained(new_pattern_i, rule_i):
    iscontained = False
    if type(new_pattern_i) == tuple or type(new_pattern_i) == list:
        set1 = set(new_pattern_i)
    else:
        set1 = set([new_pattern_i])
    if type(rule_i) == tuple or type(rule_i) == list:
        set2 = set(rule_i)
    else:
        set2 = set([rule_i])
    if set1 & set2 != set():
        return True
    else:
        return False

#print( is_contained( (1,3), (1, 2,3,4)  ) )
