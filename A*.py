#!/usr/bin/python3
from sys import path
import numpy as np
import csv
h_c = []
edges_file = []
node = []
h_f = []
edge = []
edge_cost = []
k = 1
path_cost= 0 
past_cost = []
parent = []
nbr = []
start = 1
OPEN = []
CLOSED = []
current_edges=[]
explore_edge = 0

with open('/Users/rishabhchangwani/Downloads/V-REP_scenes-2/Scene5_example/nodes.csv') as nodes :
    i = 0
    nodes = csv.reader(nodes,8, delimiter =',')
    for row in nodes:
        col = []
        if i > 7:
            OPEN.append(int(row[0]))
            col.append(int(row[0]))
            col.append(row[3])
            h_c.append(col)
            col=[]
        i+=1
N = len(h_c)
with open('/Users/rishabhchangwani/Downloads/V-REP_scenes-2/Scene5_example/edges.csv') as edges :
    i = 0
    edges = csv.reader(edges,6, delimiter =',')
    for row in edges:
        col = []
        if(i>5):
            edges_file.append([ float(x) for x in row] )
            for k in range(2,13):
                edge_cost.append(row[2])                
                if(k==int(row[0])):
                    for x in range(2):
                        col.append(int(row[x]))
                    edge.append(col)

        i+=1
# ******* Initialising Past Cost *********#
for i in range(len(OPEN)-1):
    if i == 0:
        past_cost.append(0)
    past_cost.append(10000)

    # ******** Get Child ********* #
def get_child(x):
    edge_list=[]
    for i in range(len(edge)):
        if edge[i][0] == x :
            edge_list.append(edge[i][1])
        elif edge[i][1] == x:
            edge_list.append(edge[i][0])
    return edge_list

    #******* Get Path cost *******#
# def get_path_cost(current_node, nbr):
#     for j in range(len(nbr)):
#         for i in range(len(edges_file)):
#             if(nbr[j] == edges_file[i][0] and current_node ==edges_file[i][1]) or (nbr[j] == edges_file[i][1] and current_node ==edges_file[i][0]):
#                 path_cost.append(edges_file[i][2])
#     return path_cost
    #******** Get Heuristic Cost ********* #
def get_h_c(nbr):
    cost = []
    # for i in range (len(nbr)):
    for j in range(N):
        if h_c[j][0] == nbr:
            cost = h_c[j][1]
    return float(cost)
    #******** Get Past Cost **************#
def get_past_cost(current_node,ctr):
    tentaive_cost = 0
    nbr = get_child(current_node)
    for j in range (ctr, len(nbr)):
        for i in range(len(edges_file)):
            if(nbr[j] == edges_file[i][0] and current_node ==edges_file[i][1]) or (nbr[j] == edges_file[i][1] and current_node ==edges_file[i][0]):
                path_cost = edges_file[i][2]
                index = nbr[j] - 1
                #print(nbr[j])
                # tentaive_cost = get_path_cost(current_node,nbr)
                # tentaive_cost = tentaive_cost[i]
                tentaive_cost = path_cost + past_cost[current_node-1]
                if tentaive_cost<past_cost[index]:
                    past_cost[index]=tentaive_cost
                return past_cost[index]

for i in range (1,N):
    total_cost = 0
    print(OPEN)
    current_node = OPEN[0]
    removed = OPEN.pop(0)
    CLOSED.append(i)
    nbr = get_child(current_node)
    ctr = 0
    temp = 1000
    for i in range(len(nbr)):
        #print(ctr)
        total_cost = get_h_c(nbr[i])+get_past_cost(current_node,ctr)
        ctr +=1
        print(get_past_cost(current_node,ctr))
        print(get_h_c( nbr[i]))
        print("Total cost to reach from ", current_node, " to ", nbr[i], " is ", total_cost)
        if(total_cost<temp):
            temp = total_cost
            OPEN[0]==current_node
            #print(OPEN)

# for x in range(N):
#     current_node = x+1
    
