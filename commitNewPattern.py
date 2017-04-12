#---------------------------------------------------------------
#
#   1. Read new pattern and a existing Rule Base
#   2. modify the Rule base according the new pattern.
#---------------------------------------------------------------
#   The rule base is expressed in terms of connected sets and lonly_rules
#
#---------------------------------------------------------------
import json
from intersection_functions import intersection_or_possible_rule_formation
#from optimum_partition_for_Q import *
from rulex_2 import *
#---------------------------------------------------
#     Read json 
def read(file_name):
    with open(file_name) as json_data:
        file_content = json.load(json_data)
        return file_content
#---------------------------------------------------
# Read file all_connected_sets
all_connected_sets = read('all_connected_sets.json')
print('Original connected sets:')
for i in all_connected_sets: print(i)

#--------------------------------------------------------
#  When a new pattern comes, as we already have    ------
#  the optimum partition for each connected set    ------
#  we find wich of the original connected_sets     ------
#  are intersected by the new instance             ------
#--------------------------------------------------------

def intersected_connected_sets( new_pattern, all_connected_sets ):
    indexes_of_intersected_sets = [ ]
    intersected_sets = []
    index_counter = -1
    for connected_set in all_connected_sets:
        index_counter += 1
        include_set = False
        for rule in connected_set:
            #intersects = intersection(new_pattern, rule) # INTERSECTIONS OF ALREADY RULEXED INSTANCES
            # Function that considers intersection or possible rule formation with Rulex
            intersects = intersection_or_possible_rule_formation( new_pattern, rule, 1 )
            print('The intersection of', new_pattern, 'with',rule, 'is', intersects)
            if intersects == True:
                include_set = True
        if include_set == True:
            indexes_of_intersected_sets.append( index_counter )
            intersected_sets.append( connected_set )
    return [ intersected_sets,  indexes_of_intersected_sets ]

#pattern = ( 2, 5, 'A')
#pattern = ( 5, 5, 'A')
#pattern = ( 5, 5, 'B' )
#pattern = (5, 5, 'D')
pattern = (5, 11, 'A') # Pattern for test1
#pattern = (1, 1, 'D') #Pattern with no intersections
#pattern = (4,7,'D')
[ intersected_sets,  indexes_of_intersected_sets ] = intersected_connected_sets( pattern, all_connected_sets)
print('Intersected sets', intersected_sets, 'indexes', indexes_of_intersected_sets)

#Create new set with the new pattern + intersections
def pattern_plus_intersections(pattern, intersected_sets):
        new_set = []
        for intersected_set in intersected_sets:
            for rule in intersected_set:
                new_set.append(rule)
        new_set.append(pattern)
        return new_set

print('This is the set for Rulex : ' )
new_set = pattern_plus_intersections(pattern, intersected_sets)
print(new_set)

#---------------------------------
#  Give new_set format for Rulex()
#---------------------------------
def rulex_format(new_set,risk):
    formatted = []
    for rule in new_set:
        _list = []
        for parameter in rule:
            if type(parameter) == list:
                parameter = tuple(parameter)
                _list.append(parameter)
            else:
                _list.append(parameter)
        _list.append(risk)
        the_tuple = tuple(_list)
        formatted.append(the_tuple)
    return formatted
rulex_format =  rulex_format(new_set,1)
print('Rulex of new set:', rulex(rulex_format))

#------------------------------------------------------------------------------
#           Exclude from optimim_partitions or lonly rules                   --
#           the indexes_of_intersected_sets, keep the rest of the partitions --
#------------------------------------------------------------------------------
optimum_partitions = read('optimum_partitions.json')
optimum_partitions_indexes = read('connected_rules_indexes.json')  #  They share indexes
lonly_rules = read('lonly_rules.json')
lonly_rules_indexes = read('lonly_rules_indexes.json')

print('------------------')
print('indexes of intersected sets :  ' , indexes_of_intersected_sets)
print('optimum_partitions_indexes:',optimum_partitions_indexes)
print('lonly_rules_indexes:', lonly_rules_indexes)


#  Compare the indexes of optimum_partitions (partitions for the connected rules) and lonly rules
#  with the indexes of the intersected sets
#  if they match, eliminate the entrance either in the optimim_partitions of in the lonly_rules
#  return as final set {lonly_rules, optimum_partitions}\{elements_at_indexes_of_intersected_rules}
def remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets):
    kept_partitions = []
    kept_lonly = []

    for i in range( len(optimum_partitions_indexes) ):
        index = optimum_partitions_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_partitions = kept_partitions + optimum_partitions[i]

    for i in range( len(lonly_rules_indexes) ):
        index = lonly_rules_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_lonly.append(lonly_rules[i])
    return [ kept_partitions, kept_lonly ]

print( 'Optimum partitions of the not_intersected sets : ')
not_intersected = remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets)
print(not_intersected)


"""
#---------------------------------------------------------------
#    The resulting rule base incorporating the new parrern
#    is the set { remaining_partitions U new_set }
#
#---------------------------------------------------------------
def not_intersected_union_new_set(not_intersected, new_set):
    union = []
    for i in not_intersected:
        union = union + i
    for i in new_set:
        union.append(i)
    return union
#print('result: ')
#print( not_intersected_union_new_set(not_intersected, new_set) )

#-----------------------------------------------------------------
#
#           PROCESS  ---   NEW  ---  PATTERN
#
#-----------------------------------------------------------------
#    Write json data
#--------------------------------------
def write(file_name,data):
    with open (file_name, 'w') as f:
        json.dump(data,f)

def as_tuple(iterable):
    _list = []
    for item in iterable:
        if type(item) == list:
            item = tuple(item)
            _list.append(item)
        else:
            _list.append(item)
            the_tuple = tuple(_list)
    return the_tuple

def format_new_set(new_set):
    formatted = []
    for i in new_set:
        i = as_tuple(i)
        formatted.append(i)
    return formatted

def as_list(new_set):
    _list = []
    for i in new_set:
        i = list(i)
        _list.append(i)
    return _list

def remove_risk(new_set):
    _list = []
    for rule in new_set:
        rule.pop()
        _list.append(rule)
    return _list

#--------------------------------------
def process_new_pattern(pattern):
    all_connected_sets = read('all_connected_sets.json')
    [ intersected_sets, indexes_of_intersected_sets ] = intersected_connected_sets( pattern,  all_connected_sets )
    new_set = pattern_plus_intersections(pattern, intersected_sets)
    # print('new set = pattern + intersected_Sets', new_set) 
    
    # Add risk parameter to the new (connected) set for Rules
    for rule in new_set: rule.append(1)
    #print('New connected set without RULEX', new_set)
    #FORMART INTO TUPLES
    new_set = format_new_set(new_set)
    new_set = rulex(new_set)
    print('New set after RULEX', new_set)

    new_set = as_list(new_set)
    new_set = remove_risk(new_set)  ###################
    print( 'New set for cut', new_set )
    new_set = optimum_partition( new_set )
    print('New set optimum partition', new_set)

    optimum_partitions = read('optimum_partitions.json')
    optimum_partitions_indexes = read('connected_rules_indexes.json')
    lonly_rules = read('lonly_rules.json')
    lonly_rules_indexes = read('lonly_rules_indexes.json')

    not_intersected = remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes,indexes_of_intersected_sets)
    print('Not intersected connected sets : ', not_intersected)
   # for j in not_intersected:
    #    print('j',j)
     #   for k in j: print(k)
    if new_set != False:
        new_rule_base = not_intersected_union_new_set(not_intersected,new_set)
    else:
        print('The new pattern do not intersect any connected set')
        del pattern[-1] 
        not_intersected.append( [pattern] )
        new_rule_base = not_intersected
    return new_rule_base


#pattern = [ 2,  5,  'A' ]
#print('new rule base: ', process_new_pattern(pattern))
"""
