# -*- coding: utf-8 -*-
from adjacent_matrix import *
from function_to_create_subsets import *
from create_rules import *
from functions_to_calculate_the_volume_of_a_partition import *
from break_edges import *
from compare_partitions_volumes_version1 import *

#----------------------------------------------
#    This function takes a set of rules and
#    returns the partition with higher volume
#
#    Ideally the set of rules is a connected
#    set (called Q).
#    d is a dictionary containing the steps
#    of the different partitions.
#    and leafs are those partitions situated at
#    the leafs of the tree. These are partitions
#    in which all the contradictions have been solved.
#--------------------------------------------
def optimum_partition(Q):
    [d, leafs] = tee(Q)
    if leafs != []:
        return max_volume(leafs)
    else:
        if d != {}:
            return d['1,1']
        else:
            return False # There is no partition to do. Probably the connected set has the same class.

#[d, leafs] = tee([[(9, 12), 5, 'C'], [(1, 2, 3, 8, 11), (4, 6), 'A'], [5, (4, 11), 'B']] )
#[ d, leafs ] = tee( [[(9, 12), 5, 'C'], [(1, 2, 3, 8, 11), (4, 6), 'A'], [5, (4, 5), 'B']] )
#print(d)
#print(leafs)
#print(' Optimum partition', optimum_partition( [[(9, 12), 5, 'C'], [(1, 2, 3, 8, 11), (4, 6), 'A'], [5, (4, 11), 'B']] ) )
#print('optimim partition',optimum_partition( [ [(9, 12), 5, 'C'], [(1, 2, 3, 8, 11), (4, 6), 'A'], [5, (4, 5), 'B'] ] ) )
"""
Examples:

connected_rules = [
    [(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')],
    
    [((6, 9), 11, 'A'), (8, (10, 14), 'A')],
     
    [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
    ]

Q = [(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')]
optimum_partition(Q)


Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
optimum_partition(Q)


Q = [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
optimum_partition(Q)

"""
