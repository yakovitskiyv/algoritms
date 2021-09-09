# Comment it before submitting
# class Node:
#      def __init__(self, value, next_item=None):
#          self.value = value
#          self.next_item = next_item

def solution(node, elem):
    head_node = node
    head_node_name = head_node.value
    search_node_name = elem

    if head_node_name == search_node_name:
        return 0
    idx = 0
    while node.next_item:
        node = node.next_item
        idx += 1
        if node.value == search_node_name:
            return idx
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node3")
    print(idx)
    # result is idx == 2

# test()
