from __future__ import annotations
import sys
from typing import Any, Type


class Node:
    def __init__(self, value: Any, left: Node = None, right: Node = None):
        self.value = value
        self.left = left
        self.right = right


def add_node(node, value, left, right):
    if node.value == value:
        if left != ".":
            node.left = Node(left)
        if right != ".":
            node.right = Node(right)
    else:
        if node.left:
            add_node(node.left, value, left, right)
        if node.right:
            add_node(node.right, value, left, right)


def preorder_search(node):
    if node is not None:
        print(node.value, end="")
        preorder_search(node.left)
        preorder_search(node.right)


def inorder_search(node):
    if node is not None:
        inorder_search(node.left)
        print(node.value, end="")
        inorder_search(node.right)


def postorder_search(node):
    if node is not None:
        postorder_search(node.left)
        postorder_search(node.right)
        print(node.value, end="")


n = int(sys.stdin.readline())
root = Node("A")

for i in range(n):
    value, left, right = sys.stdin.readline().split()
    add_node(root, value, left, right)

preorder_search(root)
print()
inorder_search(root)
print()
postorder_search(root)
