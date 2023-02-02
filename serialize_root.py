# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node):
    if node is None:
        return "."
    return '{}{}{}'.format(node.val, serialize(node.left), serialize(node.right))


def deserialize(data):
    if data is None:
        return None
    return helper([x for x in data], 0)


def helper(arr, t):
    if arr[t] == '.':
        return None
    root = Node(int(arr[t]))
    t += 1
    root.left = helper(arr, t)
    t += 1
    root.right = helper(arr, t)
    return root


node1 = Node(1, Node(2, Node(4, Node(7)), Node(5, Node(8, Node(10)), Node(9))), Node(3, None, Node(6)))
serialized_str = serialize(node1)
print(serialized_str)
deserialized_str = deserialize(serialized_str)
print(deserialized_str)
