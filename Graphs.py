from random import randrange

class Vertex:
  def __init__(self, value):
    self.value = value
    # Edges are held in a key, value dictionary.
    self.edges = {}

  # Add edges using a 'vertex' and assigned weight.
  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  # List edges as a list of keys for the dictionary value of the vertex.
  def get_edges(self):
    return list(self.edges.keys())

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    # Vertex is added by adding that value to the dictionary list.
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    # Add an entry to the dictionary list {from value] with an edge of {to value}.
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    # If it is bi-directional, do the same in reverse.
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    # Check to see if the current vertex matches the end vertex.
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      # If not, check the edges of the current vertex and produce a list of these edges.
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        # If these vertices have not been seen, then add them to the list of vertices we are checking.
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False


def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v_idx = randrange(0, len(vertices) - 1)
    v1 = vertices[v_idx]
    v_idx = randrange(0, len(vertices) - 1)
    v2 = vertices[v_idx]
    g.add_edge(v1, v2, randrange(1, 10))

  print_graph(g)

build_graph(False)
