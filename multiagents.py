"""
Name: Fernando Nunez
File: homework_1_search(1).py
Description: This file contains algorithms to a variety of search algorithms
Date: February 26, 2023

Help for BFS was used. I searched it up on google and found this website and used it as a guide to write my own BFS code as
well as the lecture where you explained the BFS code to us.
Website: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
 
"""


from queue import PriorityQueue
from pprint import pprint


# Graph of cities with connections to each city. Similar to our class exercises, you can draw it on a piece of paper 
# with step-by-step node inspection for better understanding 
graph = {
    'San Bernardino': ['Riverside', 'Rancho Cucamonga'],
    'Riverside': ['San Bernardino', 'Ontario', 'Pomona'],
    'Rancho Cucamonga': ['San Bernardino', 'Azusa', 'Los Angeles'],
    'Ontario': ['Riverside', 'Whittier', 'Los Angeles'],
    'Pomona': ['Riverside', 'Whittier', 'Azusa', 'Los Angeles'],
    'Whittier': ['Ontario','Pomona', 'Los Angeles'],
    'Azusa': ['Rancho Cucamonga', 'Pomona', 'Arcadia'],
    'Arcadia': ['Azusa', 'Los Angeles'],
    'Los Angeles': ['Rancho Cucamonga', 'Ontario', 'Pomona', 'Whittier', 'Arcadia']
}

# Weights are treated as g(n) function as we studied in our class lecture which represents the backward cost. 
# In the data structure below, the key represents the cost from a source to target node. For example, the first
# entry shows that there is a cost of 2 for going from San Bernardino to Riverside.
weights = {
    ('San Bernardino', 'Riverside'): 2,
    ('San Bernardino', 'Rancho Cucamonga'): 1,
    ('Riverside', 'Ontario'): 1,
    ('Riverside', 'Pomona'): 3,
    ('Rancho Cucamonga', 'Los Angeles'): 5,
    ('Pomona', 'Los Angeles'): 2,
    ('Ontario', 'Whittier'): 2,
    ('Ontario', 'Los Angeles'): 3,
    ('Rancho Cucamonga', 'Azusa'): 3,
    ('Pomona', 'Azusa'): 2,
    ('Pomona', 'Whittier'): 2,
    ('Azusa', 'Arcadia'): 1,
    ('Whittier', 'Los Angeles'): 2,
    ('Arcadia', 'Los Angeles'): 2
}

# heurist is the h(n) function as we studied in our class lecture which represents the forward cost. 
# In the data structure below, each entry represents the h(n) value. For example, the second entry
# shows that h(Riverside) is 2 (i.e., h value as forward cost for eaching at Riverside assuming that
# your current/start city is San Bernardino)

heuristic = {
    'San Bernardino': 4,
    'Riverside': 2,
    'Rancho Cucamonga': 1,
    'Ontario': 1,
    'Pomona': 3,
    'Whittier': 4,
    'Azusa': 3,
    'Arcadia': 2,
    'Los Angeles': 0
}

# Data structure to implement search algorithms. Each function below currently has one line of code
# returning empty solution with empty expanded cities. You can remove the current return statement and 
# implement your code to complete the functions.

class SearchAlgorithms:
    
    def breadthFirstSearch(self, start, goal, graph):
        """
        Search the shallowest nodes in the search tree first.

        Your search algorithm needs to return (i) a list of cities the algorithm will propose to go to to reach the
        goal, and (ii) set of expanded cities (visited nodes). Make sure to implement a graph search algorithm.

        """
        #implementing the BFS algorithm
        # initializing by putting the start node in the undiscovered queue
        undiscovered = [[start]]
        visited = []
        # while undiscovered is not empty
        while undiscovered:
            # getting the first item in the queue and making it equal to current
            path = undiscovered.pop(0)    
            current = path[-1]
            # if a node is not marked as vistied then it is marked by being put in to the visited list
            if current not in visited:
                visited.append(current)
            # if we have reached the goal state then we can print the visited nodes
            if current == goal:
                return visited
            # getting the neighbor nodes of current 
            for neighbor in graph[current]:
                # if neighbor node is has not been visited then it will add neighbor node to the end of the path
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    undiscovered.append(new_path)
        return visited
    
        
    def depthFirstSearch(self, start, goal, graph):
        """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return (i) a list of cities the algorithm will propose to go to to reach the
        goal, and (ii) set of expanded cities (visited nodes). Make sure to implement a graph search algorithm.

        Please be very careful when you expand the neighbor nodes in your code when using stack. In case of using 
        normal list or a data structure other than the Stack, you might need to reverse the order of the neighbor nodes
        before you push them in the stack to get correct results 

        """
        #implementing the DFS algorithm
        # initializing by putting the start node in the undiscovered queue
        undiscovered = [[start]]
        visited = []
        # while undiscovered is not empty
        while undiscovered:
            # getting the first item in the queue and making it equal to current
            path = undiscovered.pop(0)    
            current = path[-1]
            # if a node is not marked as vistied then it is marked by being put in to the visited list
            if current not in visited:
                visited.append(current)
            # if we have reached the goal state then we can print the visited nodes
            if current == goal:
                return visited
            # getting the neighbor nodes of current 
            for neighbor in graph[current]:
                # if neighbor node is has not been visited then it will add neighbor node to the end of the path
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    undiscovered.insert(0, new_path)
        return visited
    
            

    def uniformCostSearch(self, start, goal, graph, weights):
        """Search the node of least total cost first.
        Important things to remember
        1 - Use PriorityQueue with .put() and .get() functions
        2 - In addition to putting the start or current node in the queue, also put the cost (g(n)) using weights data structure
        3 - When you're expanding the neighbor of the current you're standing at, get its g(neighbor) by weights[(node, neighbor)] 
        4 - Calling weights[(node, neighbor)] may throw KeyError exception which is due to the fact that the weights data structure
            only has one directional weights. In the class, we mentioned that there is a path from Arad to Sibiu and back. If the 
            exception occurs, you will need to get the weight of the nodes in reverse direction (weights[(neighbor, node)])
        """
        
        #implementing the UCS algorithm
        # initializing by putting the start node in the undiscovered queue
        undiscovered = [[start]]
        visited = []
        # while undiscovered is not empty
        while undiscovered:
            # getting the first item in the queue and making it equal to current
            path = undiscovered.pop(0)    
            current = path[-1]
            # if a node is not marked as vistied then it is marked by being put in to the visited list
            if current not in visited:
                visited.append(current)
            # if we have reached the goal state then we can print the visited nodes
            if current == goal:
                return visited
            # getting the neighbor nodes of current 
            for neighbor in graph[current]:
                # if neighbor node is has not been visited then it will add neighbor node to the end of the path
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    undiscovered.append(new_path)
        return visited
    


    def AStar(self, start, goal, graph, weights, heuristic):
        """Search the node that has the lowest combined cost and heuristic first.
        Important things to remember
        1 - Use PriorityQueue with .put() and .get() functions
        2 - In addition to putting the start or current node in the queue, and the g(n), also put the combined cost (i.e., g(n) + h(n)) 
            using weights and heuristic data structure
        3 - When you're expanding the neighbor of the current you're standing at, get its g(neighbor) by weights[(node, neighbor)] 
        4 - Calling weights[(node, neighbor)] may throw KeyError exception which is due to the fact that the weights data structure
            only has one directional weights. In the class, we mentioned that there is a path from Arad to Sibiu and back. If the 
            exception occurs, you will need to get the weight of the nodes in reverse direction (weights[(neighbor, node)])
        """
        #implementing the A* algorithm
        # initializing by putting the start node in the undiscovered queue
        undiscovered = [[start]]
        visited = []
        # while undiscovered is not empty
        while undiscovered:
            # getting the first item in the queue and making it equal to current
            path = undiscovered.pop(0)    
            current = path[-1]
            # if a node is not marked as vistied then it is marked by being put in to the visited list
            if current not in visited:
                visited.append(current)
            # if we have reached the goal state then we can print the visited nodes
            if current == goal:
                return visited
            # getting the neighbor nodes of current 
            for neighbor in graph[current]:
                # if neighbor node is has not been visited then it will add neighbor node to the end of the path
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    undiscovered.append(new_path)
        return visited
    


# Call to create the object of the above class
search = SearchAlgorithms()

# Call to each algorithm to print the results
print()
print("Breadth First Search Result") # ['San Bernardino', 'Rancho Cucamonga', 'Los Angeles']
pprint(search.breadthFirstSearch('San Bernardino', 'Los Angeles', graph))
print()

print("Depth First Search Result") # ['San Bernardino', 'Riverside', 'Ontario', 'Whittier', 'Pomona', 'Azusa', 'Rancho Cucamonga', 'Los Angeles']
pprint(search.depthFirstSearch('San Bernardino', 'Los Angeles', graph))
print()

print("Uniform Cost Search Result") # ['San Bernardino', 'Rancho Cucamonga', 'Los Angeles']
pprint(search.uniformCostSearch('San Bernardino', 'Los Angeles', graph, weights))
print()

print("A* Search Result") # ['San Bernardino', 'Rancho Cucamonga', 'Los Angeles']
pprint(search.AStar('San Bernardino', 'Los Angeles', graph, weights, heuristic))
