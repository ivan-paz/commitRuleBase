# -*- coding: utf-8 -*-
from intersection_functions import intersection, sameClass

#R = [
#( (1, 2, 3, 8, 11), (4, 6), 'A'),
#( (9,12),            5,     'C'),
#(     5,             4,     'B'),
#( (2,5),             7,     'D')
#]

#def adjacent_matrix(R):
#    graph = {}
#    for i in range( len(R) ):
#        graph[str(i)] =  [ ]    
#        for j in range( len(R) ):
#            if ( i != j ) and intersection ( R[i], R[j] ) == True:
#                #print(R[i], R[j])
#                old = graph[str(i)]
#                new = old + [str(j)]
#                graph[str(i)] = new
#    return graph
#
#print(adjacent_matrix(R))

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

