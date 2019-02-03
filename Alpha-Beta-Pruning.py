import numpy as np
import math
import queue

class Node:

    def __init__(self, id, value, alpha, beta, visited, children):
        self.id = id
        self.value = value
        self.alpha = alpha
        self.beta = beta
        self.visited = visited
        self.children = children

def print_alpha_und_beta(alpha, beta):
    if alpha == -np.inf:
        print("\tAlpha = -inf")
    else:
        print("\tAlpha =", alpha)

    if beta == np.inf:
        print("\tBeta = inf")
    else:
        print("\tBeta =", beta)


def alphabeta(node, depth, alpha, beta, maximizingPlayer):


    if node.children != []:
        print("\n\n\nBetrachte den Knoten " + str(node.id) + ":")
        print_alpha_und_beta(alpha, beta)

    if depth == 0 or node.children == []:
        print("\n\n\nDer Blatt Knoten mit dem Wert", node.value, "wurde gefunden.")
        return int(node.value)

    if maximizingPlayer:
        print("\tMAX-Spieler ist an der Reihe. Das heißt, suche für Alpha einen größeren Wert.")
        value = -np.inf
        for child in node.children:
            value = max(value, alphabeta(child, depth=depth-1, alpha=alpha, beta=beta, maximizingPlayer=False))
            print("\tUpdate: Der Knoten", node.id, "bekommt den Wert", value ,"\n\t=> Alpha =", value, "(für den Knoten " + str(node.id) + ")")
            alpha = max(alpha, value)

            if alpha >= beta:
                # print("Beta-cut:", child.id)
                print("\tBeta-cut: Der Kindknoten", child.id, "(des Elternknotens", node.id, ") ist der letzte Kindknoten der untersucht werden muss. Denn der Knoten", node.id, "hat einen Wert von", value, ">=", beta, "(sein Beta Wert)")
                break
            else:
                node.value = value
        return value
    else:
        print("\tMIN-Spieler ist an der Reihe. Das heißt, suche für Beta einen kleineren Wert")
        value = np.inf
        for child in node.children:
            value = min(value, alphabeta(child, depth=depth - 1, alpha=alpha, beta=beta, maximizingPlayer=True))
            print("\tUpdate: Der Knoten", node.id, "bekommt den Wert", value, "\n\t=> Beta =", value, "(für den Knoten " + str(node.id) + ")")
            beta = min(beta, value)

            if alpha >= beta:
                # print("Alpha-cut:", child.id)
                print("\tAlpha-cut: Der Kindknoten", child.id, "(des Elternknotens", node.id, ") ist der letzte Kindknoten der untersucht werden muss. Denn der Knoten", node.id, "hat einen Wert von", value, ">=", alpha, "(sein Alpha Wert)")
                break
            else:
                node.value = value
        return value





def show_tree(tree):

    fifo = queue.Queue()
    fifo.put(tree)

    print(tree.id, end="")
    # print("Root Node:", tree.__get_id__())

    depth = -1

    while not fifo.empty():
        children = []
        while not fifo.empty():
            next_child = (fifo.get()).children

            children.extend(next_child)
        print("\n")

        for elem in children:
            print(elem.id, end="\t")
            fifo.put(elem)

        depth += 1


    return depth





def tree_1():
    leaf_7 = Node(id=11, value="7", alpha="", beta="", visited=False, children=[])
    leaf_15 = Node(id=12, value="15", alpha="", beta="", visited=False, children=[])
    leaf_20 = Node(id=13, value="20", alpha="", beta="", visited=False, children=[])
    leaf_25 = Node(id=14, value="25", alpha="", beta="", visited=False, children=[])
    leaf_16 = Node(id=15, value="16", alpha="", beta="", visited=False, children=[])
    leaf_3_left = Node(id=16, value="3", alpha="", beta="", visited=False, children=[])
    leaf_21 = Node(id=17, value="21", alpha="", beta="", visited=False, children=[])
    leaf_6 = Node(id=18, value="6", alpha="", beta="", visited=False, children=[])
    leaf_17 = Node(id=19, value="17", alpha="", beta="", visited=False, children=[])
    leaf_10 = Node(id=20, value="10", alpha="", beta="", visited=False, children=[])
    leaf_3_right = Node(id=21, value="3", alpha="", beta="", visited=False, children=[])
    leaf_12 = Node(id=22, value="12", alpha="", beta="", visited=False, children=[])
    leaf_8 = Node(id=23, value="8", alpha="", beta="", visited=False, children=[])
    leaf_13 = Node(id=24, value="13", alpha="", beta="", visited=False, children=[])
    leaf_2 = Node(id=25, value="2", alpha="", beta="", visited=False, children=[])
    leaf_11 = Node(id=26, value="11", alpha="", beta="", visited=False, children=[])

    inner_node_1 = Node(id=4, value="", alpha="", beta="", visited=False, children=[leaf_7, leaf_15])
    inner_node_2 = Node(id=5, value="", alpha="", beta="", visited=False, children=[leaf_20, leaf_25])
    inner_node_3 = Node(id=6, value="", alpha="", beta="", visited=False, children=[leaf_16, leaf_3_left, leaf_21])
    inner_node_4 = Node(id=7, value="", alpha="", beta="", visited=False, children=[leaf_6, leaf_17, leaf_10])
    inner_node_5 = Node(id=8, value="", alpha="", beta="", visited=False, children=[leaf_3_right, leaf_12])
    inner_node_6 = Node(id=9, value="", alpha="", beta="", visited=False, children=[leaf_8, leaf_13])
    inner_node_7 = Node(id=10, value="", alpha="", beta="", visited=False, children=[leaf_2, leaf_11])

    inner_node_8 = Node(id=2, value="", alpha="", beta="", visited=False, children=[inner_node_1, inner_node_2, inner_node_3])
    inner_node_9 = Node(id=3, value="", alpha="", beta="", visited=False, children=[inner_node_4, inner_node_5, inner_node_6, inner_node_7])

    root = Node(id=1, value="", alpha="", beta="", visited=False, children=[inner_node_8, inner_node_9])


    return root



if __name__ == '__main__':
    t = tree_1()
    depth = show_tree(t)
    print("Der Baum hat eine maximale Tiefe von", depth)
    print(alphabeta(t, depth=depth, alpha=-np.inf, beta=np.inf, maximizingPlayer=True))




