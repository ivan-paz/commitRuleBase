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
