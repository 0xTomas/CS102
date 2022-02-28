from heapq import heappop, heappush
from math import inf

graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


def dijkstras(graph, start):
    # Instantiating a distance dictionary that will eventually map
    # vertices to the distance from the start vertex.

    distances = {}

    # Loop through each vertex in the graph and set its corresponding
    # value within distances to infinity
    for vertex in graph:
        distances[vertex] = inf

    # Set the start vertex distance to zero.
    distances[start] = 0

    # This tuple represents the start vertex within the min-heap list.

    vertices_to_explore = [(0, start)]

    """
    First, we'll traverse the vertices_to_explore heap until it is empty, 
    popping off the vertex with the minimum distance from start.
    Inside our while loop, we'll iterate over the neighboring vertices of
    current_index and add each neighbor (and its distance from start)
    to the vertices_to_explore min-heap.
    """

    # While there are vertices to explore:
    while vertices_to_explore:
        # This will always be the vertex with the minimum distance from start
        current_distance, current_vertex = heappop(vertices_to_explore)
        print("\n This is the current vertex: {0} with the distance: {1}".format(current_vertex, current_distance))
        # Identify neighbor's distance from start
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
            print("\n This is the neighbor: {0} with the distance: {1}".format(neighbor, edge_weight))
            print("The distance from the start vertex {0} to its neighbor {1} is: {2}.".format(start, neighbor, new_distance))

            # Comparing the distances and replacing them in heap list
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))
                print("Pushing the neighbor into the Heap List...")

    return distances


distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
