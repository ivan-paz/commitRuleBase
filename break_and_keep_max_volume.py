#
#
#
#
#
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
    #print(element)
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

#---------------------------------------------------------
#           ADJACENT MATRIX
#  THAT DO NOT CONSIDER INTERSECTIONS OF
#        RULES OF THE SAME CLASS
#
#---------------------------------------------------------
def adjacent_matrix(R):
    graph = {}
    for i in range( len(R) ):
        graph[str(i)] =  [ ]    
        for j in range( len(R) ):
            if ( i != j ) and intersection( R[i], R[j] )== True and sameClass(R[i],R[j])==False:
                #print(R[i], R[j])
                old = graph[str(i)]
                new = old + [str(j)]
                graph[str(i)] = new
    return graph
#print(adjacent_matrix(R))
#adjacent_matrix( [ ((6, 9), 11, 'A'), (8, (10, 14), 'A') ] )

#
#
#      Function that recibes a couple of lists
#      labeled with different class. For example :
#
#   lists          class
#   (1,2,3,8,11) -> 0
#   (5)          -> 1

#     and returns tuples separated by the classes

#     in the example :

#     (1,2,3) -> 0
#     (5)     -> 1
#     (8,11)  -> 0
#
#
#

#  create list with format [element, class]
def create_labels(_list,_class):
    labels = list()
    if type(_list) == int or type(_list) == float:
        labels = labels + [[_list,_class]]
    else:
        for element in _list:
            pair = [element,_class]
            labels = labels  + [pair]
    return labels
#  create_labels((1,2,3,8,11),0)
#---------------------------------------------------------------------
#-------------------------------------------------------------------------------
import operator
def create_sets(_list1,_list2):
    list1 = create_labels(_list1, 0)
    list2 = create_labels(_list2, 1)
    one_list = list1 + list2
    sorted_list = sorted(one_list, key = operator.itemgetter(0))
    return sorted_list
#      create_sets((1,2,3,8,11),(5,6,9))
 
def subsets(a):
    zero = []
    #one =  []
    temp = []
    
    if a[0][1] == 0:
        classe = 0
    else:
         classe = 1
    for ele in a:
        #print(ele)
        
        if ele[1] == classe:
            temp = temp + [ ele[0] ]
            #print('ele',ele,'temporal',temp)
        else:
            #print('different class')
            #if classe == 0:
            #   zero = zero + [temp]
            #else:
            #     one = one + [temp]
            zero = zero + [temp,classe]
            classe = ele[1]
            temp = []
            temp = temp + [ele[0]]
    zero = zero + [temp,classe]
    return zero

#EXAMPLES
#a = [(1, 0), (2, 0), (3, 0), (5, 1), (8, 0),(9,0)]
#subsets(a)
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0), (9, 1), (11, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (8, 0), (9, 1), (11, 0)])  

def create_subsets(set1_class1,set2_class2):
    ordered_list = create_sets(set1_class1,set2_class2)
    list_of_subsets = subsets(ordered_list)
    return list_of_subsets

#print(      create_subsets( (1,2,3,8,11), (5))   )


# lalala
import copy
def condition(t1, t2):
    #Ckeck if t1 and t2 intersect
    set1 = set()
    set2 = set();
    if type(t1) == int or type(t1)== float:
        set1.add(t1)
    else:
        for x in t1: set1.add(x)
    if type(t2) == int or type(t2)== float:
        set2.add(t2)
    else:
        for y in t2: set2.add(y)
    if len(set1.intersection(set2)) != 0:
        return True
    else:
        return False
#condition( (4,6), 4 )
#condition((1,2,3,8,11),(9,12))

def rules_form_subsets(subsets, i, R1, R2):
    rules = [ ]
    R1 = list(R1)
    R2 = list(R2)
    for j in range(len(subsets)):
        if j%2 != 0:
            #print(subsets[j],subsets[j-1])
            if subsets[j] == 0:
                rule = copy.deepcopy(R1)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
            else:
                rule = copy.deepcopy(R2)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
    return rules
#rules_form_subsets([[1, 2, 3], 0, [5], 1, [8, 11], 0], 0, R1, R2)
def partitions(R1, R2):
    partitions = [ ]
    if R1[-1] != R2[-1]:
        for i in range(len(R1) - 1 ):
            #print(R1[i],R2[i])
            if condition(R1[i],R2[i]) == False:
                subsets = create_subsets(R1[i],R2[i])
                rules = rules_form_subsets(subsets, i, R1, R2)
                partitions = partitions + [rules]
        return partitions
    else:
        return False

#R1 = ( (1,2,3,8,11), (4,6), 'A' )
#R2 = ( 5, 4, 'B')
#print(partitions( R1, R2 ))
#R1 = ((9,12), 5, 'C')
#R2 = ( (1,2,3,8,11), (4,6), 'A' )
#partitions( R1, R2 )

# ñañañ





# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:33:38 2017

@author: ivanpaz
"""
from operator import itemgetter
#-------------------------------------------------------------------
#Calculate the volume of an individual parameter
# volume = | max - min |
def parameter_volume(parameter):
    if type(parameter) == int or type(parameter)==float:
        maximum = parameter
        minimum = parameter
    else:
        minimum = min(parameter)
        maximum = max(parameter)
    volume = abs(maximum - minimum)
    return volume
#parameter_volume(5)
#parameter_volume((11,13,16))
#-------------------------------------------------------------------
#Function to calculate the volume of a rule
def rule_volume(rule):
    volume = []
    dimension = 0
    for parameter in range(0,len(rule) -1 ):
        parameter_contribution = parameter_volume(rule[parameter])
        if parameter_contribution != 0:
            dimension = dimension + 1
            volume = volume + [parameter_contribution]
            #print('volume:',volume)
    volume = sum(volume)
    return [volume,dimension]
#rule_volume((12, (10, 13), 'B'))
#-------------------------------------------------------------------
# Function that recibes an array with the [volume,dimension] for a set of rules
# and return the global [volume,dimension] for each dimension
def sum_equal_dimensions(volumes):
    total_volumes_and_dimensions = []
    while len(volumes) > 0:
        temporal = volumes[0]
        volumes.remove(temporal)
        for element in volumes:
            if temporal[1] == element[1]:
                temporal[0] = temporal[0] + element[0]
                volumes.remove(element)
        total_volumes_and_dimensions = total_volumes_and_dimensions + [temporal]
    return total_volumes_and_dimensions
#sum_equal_dimensions( [ [4.0, 2], [3.0, 1], [1.0, 1]  ] )
#sum_equal_dimensions([[3.0, 1], [4.0, 2], [1.0, 1]])
#-------------------------------------------------------------------
#Function that takes an array of arrays and sort them by its second entrance
#from operator import itemgetter

def sort_volumes(volumes):
    volumes = sorted(volumes,key=itemgetter(1))
    return volumes
#sort_volumes([[4.0, 1], [4.0, 2]])
#sort_volumes([[4.0, 2], [4.0, 1]])
#-------------------------------------------------------------------
#Function to calculate the volume of a set of rules
# For each rule in the set
    #calculate its volume
#retur the sum of the volumes
def partition_volume(rules):
    volumes = []
    for rule in rules:
        volume = rule_volume(rule)
        volumes = volumes + [volume]
    volumes = sum_equal_dimensions(volumes)
    volumes = sort_volumes(volumes)
    return volumes
#partition_volume([(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D'), ((12,13),10,'B')])


#
#
#
#
#         Functions to calculate the volume of a set of rules 
#
#
#
#
from operator import itemgetter

#    FUNCTION TO CALCULATE THE VOLUME OF A PARAMETER
def parameter_volume(parameter):
    if type(parameter) == int or type(parameter) == float:
        minimum = maximum = parameter
    else:
        minimum = min(parameter)
        maximum = max(parameter)
    volume = abs(maximum - minimum)
    return volume
#print(parameter_volume((5,)))
#print(parameter_volume((11,13,16)))
#print(parameter_volume({11,13,16}))

#Function to calculate the volume of a rule
def rule_volume(rule):
    volume = []
    dimension = 0
    for parameter in range(0,len(rule) -1 ):
        parameter_contribution = parameter_volume(rule[parameter])
        if parameter_contribution != 0:
            dimension = dimension + 1
            volume = volume + [parameter_contribution]
            #print('volume:',volume)
    volume = sum(volume)
    return [volume,dimension]
#print(rule_volume([{12}, {10, 13}, 'B']))
#print(rule_volume([{12,13}, {10, 13}, 'B']))
#print(rule_volume([{8}, (3,), 'A']))
#print(rule_volume([8, (5,), 'B']))
#print(rule_volume([{8}, (7,), 'A']))



#-------------------------------------------------------------------
# Function that receives an array with the [volume,dimension] for a set of rules
# and return the global [volume, dimension] for each dimension
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
def sum_equal_dimensions(volumes):
    dimensions = {}
    result = []
 #   print(volumes)
    for volume in volumes:
        key = str(volume[1])
 #       print(type(key))
 #       print(key)
        if key not in dimensions:
            dimensions[key] = [0,int(key)]
#    print('the dimensions are:',dimensions)
    while len(volumes) > 0:
        temporal = volumes[0]
        volumes.remove(temporal)
        temporalkey = str(temporal[1])
        suma = dimensions[temporalkey]
        suma[0] = suma[0] + temporal[0]
        dimensions[temporalkey] = suma
    #print(dimensions)
    for key in dimensions:
        result.append(dimensions[key])
    return result    
#print(sum_equal_dimensions( [ [4.0, 2], [3.0, 1], [1.0, 1]  ] ) )
#print(sum_equal_dimensions([[3.0, 1], [4.0, 2], [1.0, 1]]) )
#print(sum_equal_dimensions([[0,0],[0,0],[0,0]]))
#print(sum_equal_dimensions([[2, 1], [0, 0], [2, 1], [0, 0], [0, 0], [0, 0]]))
#-------------------------------------------------------------------
#Function that takes an array of arrays and sort them by its second entrance
#from operator import itemgetter

def sort_volumes(volumes):
    volumes = sorted(volumes,key=itemgetter(1))
    return volumes
#sort_volumes([[4.0, 1], [4.0, 2]])
#sort_volumes([[4.0, 2], [4.0, 1]])
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]))
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]) )
#print(sort_volumes([[0, 0]]))
#-------------------------------------------------------------------
#Function to calculate the volume of a set of rules
# For each rule in the set
    #calculate its volume
#retur the sum of the volumes
def volume_of_the_ruleset(rules):
    volumes = []
    for rule in rules:
#        print(rule)
        volume = rule_volume(rule)
#        print('aportacion de la regla', volume)
        volumes = volumes + [volume]
#    print('volumes',volumes)
    volumes = sum_equal_dimensions(volumes)
    volumes = sort_volumes(volumes)
    return volumes
#print(partition_volume([[(12,), {10, 13}, 'B'], [{11, 13}, {11, 13}, 'D'], [{12,13},(10,),'B'] ]))
#print(volume_of_the_ruleset( [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A'], [{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A'] ] ) )
#
#from calculate_volume_of_a_ruleset import volume_of_the_ruleset, sum_equal_dimensions
def partition_volumes(combinations):
    combinations_volumes = []
    for combination in combinations:
        combination_volume = []
        #print('combination\n', combination)
        # Each partition is the partition of a rule
        for partition in combination:
            volume_of_the_partition = volume_of_the_ruleset(partition)
            [combination_volume.append(x) for x in volume_of_the_partition]
#        print('combination volume',combination_volume)
        combination_volume = sum_equal_dimensions(combination_volume)
#        print('combination volume',combination_volume)
        combinations_volumes.append(combination_volume)
    return combinations_volumes
# -*- coding: utf-8 -*-
"""

Function that takes a set of sets of rules, each one corresponding
to a different partition of an original connected set

e.g set1, set2, set3 . . .

and return the set (partition) with greater "volume".


"""
from copy import deepcopy
#-----------------------------------------------
# Function "compare" takes two single volumes
# that could have different volume and dimension
# [volume1, dimension1] [volume2, domension2]
# and returns the maximum considering volume
# and dimension.
#-----------------------------------------------
def compare(vol1,vol2):
    if vol1[1] > vol2[1]:
        return 1
    elif vol1[1] < vol2[1]:
        return 2
    elif vol1[0] > vol2[0]:
        return 1
    elif vol1[0] < vol2[0]:
        return 2
    else:
        return 3

#print(compare([4,1],[3,1]))

#-------------------------------------------------
#  This function takes two volumes (one beguins being the
#  winner and the other the contendent) that may have
#  different dimensions e.g [[0,0],[2,1],[2,4]] and [[3,1],[1,4]]
#  and returns:
#  1  if the winner has the bigger volume.
#  2  if the contendent has the bigger volume.
#  3  if they are tie .
#  They fight to see which one winns.
#-------------------------------------------------
def fight(winner, contendent):
    winner_copy = deepcopy(winner)
    contendent_copy = deepcopy(contendent)

    hand1 = winner[-1]
    hand2 = contendent[-1]
    result = 3

    while result == 3 and len(winner) > 0 and len(contendent) > 0:
        hand1 = winner[-1]
        del winner[-1]
        hand2 = contendent[-1]
        del contendent[-1]

        result = compare(hand1, hand2)
        if result == 1:
            return winner_copy
        if result == 2:
            return contendent_copy
        if result == 3:
            result = 3
    if result == 3:
        return winner_copy
    else:
        return result
#print( fight( [[0,0],[5,1],[4,2]], [[10,1],[4,2]]) )
#print(fight([[0,0],[1,2]],[[0,0]]))
#print(fight( [[4, 1], [0, 0]], [[8, 1], [0, 0]]))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#   This function receives an array with the volumes of the different
#   combinations created from the different partitions of the rules 
#   -the different ways of solving the contradictions-
#   and return the index of the bigest one
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#def find_combination_with_maximum_volume(volumes_of_the_combinations):
#    if volumes_of_the_combinations:
#        maximum_volume = volumes_of_the_combinations[0]
#    for i in range(len(volumes_of_the_combinations)):
#        maximum_volume = fight(maximum_volume,volumes_of_the_combinations[i])
#    for i, j in enumerate(volumes_of_the_combinations):
#        if j == maximum_volume:
#            index = i
#    print(i)
#    return i
def find_combination_with_maximum_volume(volumes_of_the_combinations):
    if volumes_of_the_combinations:
        maximum_volume = volumes_of_the_combinations[0]
    if len(volumes_of_the_combinations)==1:
        return 0
    for i in range(len(volumes_of_the_combinations)):
        maximum_volume = fight(maximum_volume,volumes_of_the_combinations[i])
    for i, j in enumerate(volumes_of_the_combinations):
        if j == maximum_volume:
            index = i
    return i



def exclude_current_edge(edge,edges):
    temp = copy.deepcopy(edges)
    temp.remove(edge)
    return temp


import itertools


def create_combinations_from_rule_partitions(partitions):
    combinations = list(itertools.product(*partitions))
    #[print(c) for c in combinations]
    return combinations


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

#graph = {'0': ['1', '2'], '1': ['0'], '2': ['0']}
#print(generate_edges(graph))

def simplify_edges(edges):
    simplified_edges = [ ]
    for edge in edges:
        if ( (edge[0],edge[1]) and (edge[1],edge[0]) ) not in simplified_edges:
            simplified_edges = simplified_edges + [edge]
    return simplified_edges
#    simplify_edges(edges)




def all_partitions(rule_set):
    all_partitions = []
    #print('Connected_set to break tree-like :', rule_set)
    matrix = adjacent_matrix(rule_set)
    #print('Matrix', matrix)
    edges = generate_edges(matrix)
    edges = simplify_edges(edges)
    #print('Edges', edges)
    for i in range(len(edges)): edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
  
    P = [ ]
    for edge in edges:
        #print('breaking', edge)
        temp_P = [ ]
        #print('partitions of rules: ', rule_set[ int(edge[0]) ], rule_set[ int(edge[1]) ] )
        # save all the partitions
        all_partitions.append( partitions( rule_set[ int(edge[0]) ], rule_set[ int(edge[1]) ]))
    return all_partitions

#reglas = [(3, 7, 'B'), ((1, 4), (6, 8), 'A'), ((2,5),(5,9),'A')]
#print(all_partitions(reglas))


def solve_contradictions_seek_maximum_volume(rule_set):
    all_the_partitions = all_partitions(rule_set)
    combinations_of_the_partitions = create_combinations_from_rule_partitions(all_the_partitions)
    index_of_the_combination_with_maximum_volume = find_combination_with_maximum_volume( partition_volumes( combinations_of_the_partitions  ))
    print( 'comb with max vol',combinations_of_the_partitions[index_of_the_combination_with_maximum_volume])
    return combinations_of_the_partitions[index_of_the_combination_with_maximum_volume]

cores_to_break = [(3, 7, 'B'), ((1, 4), (6, 8), 'A'), ((2,5),(5,9),'A')]
solve_contradictions_seek_maximum_volume(cores_to_break)





















