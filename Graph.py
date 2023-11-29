class Node:
    def __init__(self, value=None, neighbors=None):
        self.value = value
        self.neighbors = neighbors

    def __str__(self):
        return str(self.value)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)
        neighbor.neighbors.remove(self)


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes
