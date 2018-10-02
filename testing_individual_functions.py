#
#    testing function that finds intersected sets or possible rule formation given:
#    a set_of_rules
#    a new pattern
#    a d
#
#
from intersection_functions import intersection_or_possible_rule_formation

#--------------------------------------------------------
#  When a new pattern comes, as we already have    ------
#  the optimum partition for each connected set    ------
#  we find wich of the original connected_sets     ------
#  are intersected by the new instance             ------
#--------------------------------------------------------
def intersected_connected_sets( new_pattern, all_connected_sets, d ):
    indexes_of_intersected_sets = [ ]
    intersected_sets = []
    index_counter = -1
    for connected_set in all_connected_sets:
        index_counter += 1
        include_set = False
        for rule in connected_set:
            # Function that considers intersection or possible rule formation with Rulex
            intersects = intersection_or_possible_rule_formation( new_pattern, rule, d )
            print('The intersection of', new_pattern, 'with',rule, 'is', intersects)
            if intersects == True:
                include_set = True
        if include_set == True:
            indexes_of_intersected_sets.append( index_counter )
            intersected_sets.append( connected_set )
    return [ intersected_sets,  indexes_of_intersected_sets ]

#pattern = ( 2, 5, 'A')
#pattern = ( 5, 5, 'A')
#pattern = ( 5, 5, 'B' ) # Pattern Test 1 
pattern = (5, 5, 'D')   # Pattern for Test 3
#pattern = (5, 11, 'A')  # Pattern for Test 2
pattern = (1, 1, 'D')   # Pattern with no intersections
#pattern = (4,7,'D')

patterns = [
	(1,1,'D'),
	(0,3,'D'),
	(3,2,'D'),
	(4,3,'D'),
	(5,1,'D'),
]

#     working again on this repo on Oct 2nd 2018
all_connected_sets = [ [[ [0,5], 2, 'D']] ]
[print('this is a connected set: ',connected_set) for connected_set in all_connected_sets]

for pattern in patterns:
    [ intersected_sets,  indexes_of_intersected_sets ] = intersected_connected_sets( pattern, all_connected_sets, d = 1)
    print('Intersected sets', intersected_sets, 'indexes', indexes_of_intersected_sets)





























