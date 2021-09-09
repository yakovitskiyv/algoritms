# Comment it before submitting
# class Node:
# def __init__(self, value, next_item=None):
# self.value = value
# self.next_item = next_item


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


def print_node(node):
    while node:
        print(node.value)
        node = node.next_item


def get_node_by_index(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node


def solution(node, idx):
    cur_node = get_node_by_index(node, idx)

    if idx == 0:
        head_node = get_node_by_index(node, idx+1)
        # print_node(head_node)
        return head_node
    if cur_node.next_item is None:
        previous_node = get_node_by_index(node, idx-1)
        previous_node.next_item = None
        # print_node(node)
        return node
    else:
        previous_node = get_node_by_index(node, idx-1)
        next_node = get_node_by_index(node, idx+1)
        previous_node.next_item = next_node
        # print_node(node)
        return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)

    # result is node0 -> node2 -> node3
# test()
