import sys

import matplotlib.pyplot as plt
import networkx as nx
import pprint


class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.__str__()

class Edge:
    def __init__(self, n1: Node, n2: Node, price: int):
        self.start = n1
        self.end = n2
        self.edge = (n1, n2)
        self.price = price

    def __str__(self):
        return f"{self.start} ==> {self.end} "

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.price <= other.price

class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.visual = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, n1: Node, n2: Node, price: int):
        new_edge = Edge(n1, n2, price)
        n1.edges.append(new_edge)
        self.visual.append(new_edge)

    def is_adjacent(self, n1, n2):
        for e in n1.edges:
            if n2 in e.edge:
                return True
        return False

    def visualize(self):
        G = nx.Graph()
        edges = [(e.start.data, e.end.data, {"label": e.price}) for e in self.visual]
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def dfs(self, start, end):
        path = []
        visited = []
        all_paths = []
        self._dfs_rec(start, end, visited, path, all_paths)
        return all_paths

    def _dfs_rec(self, start, end, visited, path, all_paths):
        visited.append(start)
        if start == end:
            all_paths.append(path.copy())
        for edge in start.edges:
            neighbor = edge.end
            if neighbor not in visited:
                path.append(edge)
                self._dfs_rec(neighbor, end, visited, path, all_paths)
                path.pop()
        visited.remove(start)


    def display_all_paths(self, n1, n2):
        self.get_all_paths(n1, n2)
        # print(f"option ~ {counter} ~ ")
        # print("")
        # print(f"from {start} to {end}")
        # print(edge)
        # print(f'{tot_price} $')

    def get_all_paths(self, start, end):
        dfs_ret = self.dfs(start, end)
        if dfs_ret is None:
            return {}
        all_paths = {}
        for i, path in enumerate(dfs_ret):
            tot_price = 0
            for q, edge in enumerate(path):
                # for edge in path[node].edges:
                    if edge.end == end or path[q + 1].start:
                        tot_price += edge.price
            all_paths[f"path num {i + 1}"] = {"path": path, "price": tot_price}
        return all_paths

    def cheapest(self, start, end):
        # cheapest = [p for p in graph.display_all_paths(from_node, to_node).values() if min([e.price for e in p[1:]])]
        all = self.get_all_paths(start, end)
        cheapest = min(all)
        print(cheapest, all[f'{cheapest}']['path'], all[f'{cheapest}']['price'],"$")
        # print(f"path number {all[cheapest].index()} for {cheapest} $")
        #
        # x = float('inf')  # or sys.float_info.max
        # curr = None
        # for e in graph.display_all_paths(from_node, to_node).values():
        #     if e < x:
        #         x = e[1]
        #         curr = e
        # cheapest = curr
        # return f'cheapest path from {from_node} to {to_node} is {cheapest[0]} for {cheapest[1]}$'


graph = DirectedGraph()
B = Node('Brussels')
T = Node('Tokyo')
Tel = Node('Tel-aviv')
P = Node('Paris')
L = Node('London')
graph.add_node(B)
graph.add_node(T)
graph.add_node(Tel)
graph.add_node(P)
graph.add_node(L)
graph.add_edge(B, T, 1)
graph.add_edge(L, P, 1)
graph.add_edge(B, Tel, 2)
graph.add_edge(P, L, 3)
graph.add_edge(B, L, 4)
graph.add_edge(P, T, 5)
graph.add_edge(L, Tel, 6)
graph.add_edge(T, B, 7)
graph.add_edge(T, Tel, 8)
graph.add_edge(T, P, 9)
graph.add_edge(P, Tel, 10)
graph.add_edge(Tel, B, 11)
graph.add_edge(Tel, L, 12)
graph.add_edge(Tel, T, 12)
# for node in graph.nodes:
#     print(node)
#     for edge in node.edges:
#         print(edge)

# print(graph.is_adjacent(Tel, T))
# [print(e) for e in Tel.edges]
# pprint.pprint(graph.display_all_paths(P, L))
# print(graph.dfs(P,L))
pprint.pprint(graph.get_all_paths(P, L))
# graph.cheapest(P,L)
# print(graph.cheapest(P,L))
# print(graph.cheapest(P, L))
#
# graph.visualize()