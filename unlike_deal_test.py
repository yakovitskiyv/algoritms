class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def solution(node, idx):
    cur_node = get_node_by_index(node, idx)

    if idx == 0:
        head_node = get_node_by_index(node, idx+1)
        return head_node
    if cur_node.next is None:
        previous_node = get_node_by_index(node, idx-1)
        previous_node.next = None
        return node

    previous_node = get_node_by_index(node, idx-1)
    next_node = get_node_by_index(node, idx+1)
    previous_node.next = next_node
    return node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)

    # result is node0 -> node2 -> node3

test()