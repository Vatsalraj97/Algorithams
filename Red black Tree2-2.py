import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class RedBlackTree:
    def __init__(self):
        self.null_node = Node(0)
        self.null_node.color = 0
        self.null_node.left = None
        self.null_node.right = None
        self.root = self.null_node

    def pre_order(self, node):
        if node != self.null_node:
            sys.stdout.write(str(node.item) + " ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node(self, key):
        node=self.get_root()
        z = self.null_node
        while node != self.null_node:
            if node.item == key:
                z = node
            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.null_node:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.null_node:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.null_node:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fix_delete(x)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def print_tree(self, node=None, indent="", is_last=True):
        if node is None:
            node = self.root

        if node != self.null_node:
            child_indent = indent + "    "
            self.print_tree(node.right, child_indent, False)

            marker = "└── " if is_last else "├── "
            color = "R" if node.color == 1 else "B"
            print(f"{indent}{marker}{node.item} ({color})")

            self.print_tree(node.left, child_indent, True)

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        print (node.item)
        return node

    def maximum(self, node):
        while node.right != self.null_node:
            node = node.right
        print (node.item)
        return node

    def successor(self, x):
        if x.right != self.null_node:
            return self.minimum(x.right)

        y = x.parent
        while y != self.null_node and x == y.right:
            x = y
            y = y.parent
        print(y.item)
        return y
        
    def predecessor(self, x):
        if x.left != self.null_node:
            return self.maximum(x.left)

        y = x.parent
        while y != self.null_node and x == y.left:
            x = y
            y = y.parent
        print(y.item)
        return y
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        y = None
        x = self.root

        while x != self.null_node:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)
    def find_node(self, value):
        node = self.root
        while node != self.null_node:
            if node.item == value:
                return node
            elif node.item < value:
                node = node.right
            else:
                node = node.left
        else:
            print("node not found")

    def get_root(self):
        return self.root



    

   
