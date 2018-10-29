#------------------------------------------------------------
#
#    This function takes a rule Set and separates it into
#    its connected Components, i.e. into sets with rules
#    which intersects among them
#
#------------------------------------------------------------

#Example1
#ruleSet = [
#        #Component 1
#	[ {1,3},   {3,5},  'A'],
#	[ {2,5},   {4},    'A'],
#	[ {2},     {2,6},  'A'],
#        #Component 2
#	[ {5.5,9}, {1},    'A'],
#        [ {7},  {0.5,2.5}, 'A'],
#        #Component 3
#        [ {8},     {4.5},  'A']
#]

#Example 1.1
#ruleSet = [
#        #Component 1
#        [ {1,3},   {3,5},  'A'],
#        [ {2,5},   {4},    'A'],
#        [ {4},     {2,6},  'A'],#this has been moved
#        #Component 2
#        [ {5.5,9}, {1},    'A'],
#        [ {7},  {0.5,2.5}, 'A'],
#        #Component 3
#        [ {8},     {4.5},  'A']
#]

#Example2
#ruleSet = [
#[ {1, 2, 3, 8, 11}, {4, 6},   'A'],
#[ {9,12},            {5},     'A'],
#[    {5},            {4},     'A'],
#[ {2,5},             {7},     'A']
#]


#Ejemple3
#ruleSet = [
# [{2, 4}, {3, 5}, 'i'],
# [{6, 7}, {4}, 'i']
#]
#-------------------------------------------------------------
#                   f u n c t i o n s
#------------------------------------------------------------


# This function finds the minimum and maximum values
# of a set containing numbers
# For strings call another function 
def findMinMax(_set):
    minimum = min(_set) 
    maximum = max(_set)
    return [minimum,maximum]

#   Function that returns True if two rules of the same class intersect each other
def intersection(rule1,rule2):
    intersections = 0
    if rule1[-1] == rule2[-1]:

        for p in range(len(rule1) - 1):
            [a,b] = findMinMax(rule1[p])
            [x,y] = findMinMax(rule2[p])
            if b >= x and a <= y:
                intersections+=1
        if intersections == len(rule1) - 1:
            return True
        else:
            return False
    else:
        return False

#def intersection(rule1,rule2):
#    intersections = 0
#    for p in range(len(rule1) - 1):
#        [a,b] = findMinMax(rule1[p])
#        [x,y] = findMinMax(rule2[p])
#        if b >= x and a <= y:
#            intersections+=1
#    if intersections == len(rule1) - 1:
#        return True
#    else:
#        return False
#print(intersection([{1,3},{3,5},'A'],[{2,5}, {4}, 'A']) )
#print(intersection([ {1, 2, 3, 8, 11}, {4, 6},   'A'],[    {5},            {4},     'B']))
#print(intersection([{1},{1,2},'A'],[{1}, {1,2,4}, 'A']) )

def createConnectedComponents(ruleSet):
    connectedComponents = []
    while ruleSet:
        r = ruleSet[0]
        ruleSet.remove(r)
        component = []
        component.append(r)
        for r2 in ruleSet:
            if intersection(r,r2):
                component.append(r2)
                ruleSet.remove(r2)
        connectedComponents.append(component)
    return connectedComponents
    


#def createConnectedComponents(ruleSet):
#    connectedComponents = [ ]
#
#    while ruleSet:
#        r = ruleSet[0]
#        ruleSet.remove(r)
#        #change intersected = [] by a variable
#        intersected = [ ]
#        intersected.append(r)
#
#        connectedComponent = []
#        connectedComponent.append(r)
#        
#        while intersected:
#            rule1 = intersected[0]
##            print('comparando r', rule1, 'with the ruleSet',  ruleSet)
#
#            for i in range( len(ruleSet) - 1 ):
#                rule2 = ruleSet[i]
##                print('comparing', rule1, rule2)
#                if intersection( rule1, rule2 ) and rule1!=rule2:
#                    print('intersection')
#                    connectedComponent.append(rule2)
#            print('connectedComponent',connectedComponent)
#            intersected.remove(rule1)
##        print('--------------------------------------')
##        print('connected component', connectedComponent )
#        subset = False
#        for element in connectedComponents:
#            #si al menos uno esta en el componente anterior agrega las que no estan FALTA*********
#            for x in element:
#               if x in connectedComponent:
#                   [connectedComponent.append(x) for x in element if x not in connectedComponent]
#            #if its a subset don't do anything
#            if all(x in element for x in connectedComponent):
#                subset = True
#        if subset == False:
#            connectedComponents.append(connectedComponent)
#    
#    #Delete lists that are contained in others
#    #finalConnectedComponents = []
#    for component1 in connectedComponents:
#        #is_subset=False
#        for component2 in connectedComponents:
#            if component1 != component2 and all(x in component2 for x in component1):
##                print('this list is a subset', component1)
#                connectedComponents.remove(component1)
#                #is_subset = True
#            #elif component1 not in finalConnectedComponents and is_subset == False:
#             #   finalConnectedComponents.append(component1)
##    print('final connected components : ')
#    [print(i) for i in connectedComponents]
#    return connectedComponents


#ruleSet = [  [{1}, {1, 2}, 'A'], [{2}, {2}, 'B'], [{3}, {1, 2}, 'A'], [{1}, {1, 2, 4}, 'A']  ]
#print('using the following rule set',ruleSet)
#conn = createConnectedComponents(ruleSet)
#print(conn)
