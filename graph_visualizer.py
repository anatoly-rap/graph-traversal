import queue
import networkx as nx
import matplotlib.pyplot as plt
import time
import ast
def order_bfs(graph, rtNode):
    vis, q = set(), queue.Queue()
    q.put(rtNode)
    order = []
    while not q.empty():
        vertex = q.get()
        if vertex not in vis:
            order.append(vertex)
            vis.add(vertex)
            for node in graph[vertex]:
                if node not in vis:
                    q.put(node)
    return order

def order_dfs(graph, rtNode, vis = None):
    if vis is None:
        vis = set()
    order = []
    if rtNode not in vis:
        order.append(rtNode)
        vis.add(rtNode)
        for node in graph[rtNode]:
            if node not in vis:
                order.extend(order_dfs(graph, node, vis))
    return order

def visualizer(order, title, G, position):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start = 1):
        plt.clf()
        plt.title(title)
        nx.draw(G, position, with_labels = True, node_color = ['r' if n == node else 'g' for n in G.nodes] )
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(0.5)

def gen_rand_connected_graph(nodes, edges):
    while True:
        G = nx.gnm_random_graph(nodes, edges)
        if nx.is_connected(G): return G


#main, how we call and render. 

G = nx.Graph()
graph_str = input("input graph in format: {rt: [neigh1,...], node1: [n2...]}: ")
graph_dict = ast.literal_eval(graph_str)
edges = [(key, neighbor) for key, neighbors in graph_dict.items() for neighbor in neighbors]

G.add_edges_from(edges)
#G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
pos = nx.spring_layout(G)
visualizer(order_dfs(G, 'A'), 'DFS Visualization', G, pos)
