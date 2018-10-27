
#
#    this function receives a list with tuples - or tuples with tuples -
#    and return a list of lists with sets at each parameter.  i.e.  transform the data into setRulex_format
#
#

#    Examples
#new_set = [(1, 1, 'A'), (1, 2, 'A'), (3, 1, 'A'), (3, 2, 'A'), (1, 4, 'A')]
#new_set = [(1, 1, 'A'), (1, 2, 'A'), (3, 1, 'A'), (3, 2, 'A'), (1, 4, 'A'),  ((6,7),2,'B') ]

#new_set = [[[1, 3], [1, 2], 'A'], [1, [1, 2, 4], 'A'], (2, 2, 'B')]

def convert_to_setRulex_format_func(new_set):
    setRulex_format = []
    for rule in new_set:
        temporal_list = []
        for i in range(len(rule) -1):
            #print('type', rule[i], type(rule[i]))
            if type(rule[i]) != tuple and type(rule[i]) != list:
                temporal_list.append(  set([rule[i]])  )
            else:
                temporal_set = set([])
                [temporal_set.add(j) for j in rule[i] ]
                temporal_list.append(temporal_set)
        temporal_list.append(rule[-1])
        #print(temporal_list)
        setRulex_format.append(temporal_list)
    print(setRulex_format)
    return setRulex_format 
#convert_to_setRulex_format_func(new_set)
