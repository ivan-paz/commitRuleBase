import itertools
import copy
#rule = [1, [2,3], 'A']
#rule = [[1,4], [5,6], 'B']
def expand_rule(rule):
    rule = copy.deepcopy(rule)
    expanded_rule = []
    for i in range(len(rule)):
        if type(rule[i]) != list:
            rule[i] = [rule[i]]
    for i in itertools.product(*rule):
        expanded_rule.append(i)
    return expanded_rule
#print(expand_rule(rule))

