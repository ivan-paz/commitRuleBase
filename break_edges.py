# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:25:56 2017

@author: ivan
"""
from adjacent_matrix import *
#from create_partitions_from_connected_component import *
from function_to_create_subsets import *
from create_rules import *
from functions_to_calculate_the_volume_of_a_partition import *
#from intersection_of_rules import *
from generate_edges import *

def exclude_current_edge(edge,edges):
    temp = copy.deepcopy(edges)
    temp.remove(edge)
    return temp

#Q = [
#        ( (1,2,3,8,11), (4,6), 'A'),
#        (       (9,12),     5, 'C'),
#        (            5,     4,'B')    
#    ]

#  This function receives a set "Q" with connected rules
#  and solve the contradictions
#

global ALL_PARTITIONS
ALL_PARTITIONS = []

def cut(Q):
    print('Connected_set to break tree-like :', Q)
    matrix = adjacent_matrix(Q)
#    print('Matrix', matrix)
    edges = generate_edges(matrix)
    edges = simplify_edges(edges)
    print('Edges', edges)

    for i in range(len(edges)): edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
  
    P = [ ]
    for edge in edges:
        print('breaking', edge)
        temp_P = [ ]
        print('partitions of rules: ', Q[ int(edge[0]) ], Q[ int(edge[1]) ] )
        # save all the partitions take their combinations and select the combination with
        #maximum volume
        ALL_PARTITIONS.append( partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  ) )
        temp_P = temp_P + partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  )
        print(temp_P)
        clone_Q = copy.deepcopy(Q)
        clone_Q.remove(Q[int(edge[0])])
        clone_Q.remove(Q[int(edge[1])])
        print('clone_Q', clone_Q)
        
        for p in temp_P:
            for x in clone_Q:
                p.append(x)
            print('p: ',p)
            P.append(p) #########  Eliminate levels Rompe la herarquia
    return P
Q = [(3, 7, 'B'), ((1, 4), (6, 8), 'A')]
Q = [(3, 7, 'B'), ((1, 4), (6, 8), 'A'), ((2,5),(5,9),'A')]
cut(Q)
print('ALL PARTITIONS ::')
[print(partitions) for partitions in ALL_PARTITIONS]

import itertools

partitions =  [
        [
        [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']],
        [[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']]
        ],
        [[[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]]
        ]

def create_combinations_from_rule_partitions(partitions):
    combinations = list(itertools.product(*partitions))
    #[print(c) for c in combinations]
    return combinations
combinaciones_de_las_particiones = create_combinations_from_rule_partitions(ALL_PARTITIONS)
print('------------------------------------------------------------')
[print(combination) for combination in combinaciones_de_las_particiones]



#   FIND the combination of partitions with MAXIMUM VOLUME
from combination_with_greatest_area import partition_volumes
from combination_with_greatest_area import find_combination_with_maximum_volume
index_of_the_combination_with_maximum_volume = find_combination_with_maximum_volume( partition_volumes(combinaciones_de_las_particiones))

print('------------------------------------')
print(combinaciones_de_las_particiones[index_of_the_combination_with_maximum_volume])



"""
Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
"""
#----------------------------------------------------
#   a = np.array([(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')], dtype = object)
import numpy as np
def shape(a):
    a = np.array(a,   dtype = object) # dtype = object
    return(a.shape)

#--------------------------------------------------
#          ORIGINAL WORKING FUNCTION
#---------------------------------------------------
def tee(q):
    tree_leafs = []
    i = 0
    d = {}
    leafs = True
    while leafs == True:
        j = 0
        leafs = False
        if len(shape(q)) == 1:
            print('Case1 ' , q)

            temp1 = []
            
            i = i + 1
            
            for element in q:    
                temp = cut(element)
                
                
                for k in temp:
                    j = j + 1
                    d[str(i)+ ',' +str(j)] = k
                    
                
                temp1 = temp1 + temp
                if temp != []:
                    leafs = True
                else:
                    new_leaf = element
                    print('LEAF: ', element)
                    tree_leafs.append(new_leaf)
                    
            temp = temp1
            q = temp ###
        else:
            print('Case2', q)
            temp = cut(q)
            leafs = True
            q = temp
            
            i = i + 1
            for k in q:
                j = j + 1
                d[str(i)+ ',' +str(j)] = k
    #print('leafs' , tree_leafs)
    return [d, tree_leafs]

#Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
#Q = [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
#d  = tee(Q)
#Q = [(3, 7, 'B'), ((1, 4), (6, 8), 'A')]
#[d, leafs] = tee(Q)
#print(d)
#print(leafs)
#for leaf in leafs:
#    print(leaf)
#----------------------------------------------------------------------------
