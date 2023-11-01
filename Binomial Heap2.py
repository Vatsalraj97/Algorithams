class HeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

class HeapManager:
    def __init__(self):
        self.roots = [None]*10
        self.min=HeapNode(0)

    def insert(self,key):
        new_node = HeapNode(key)
        self.add_value(new_node) 
    def add_value(self, _node):
        new_node = _node
        if new_node.key>self.min.key:
            self.min=new_node
        order = 0
        filled=False
        while filled==False:
            
            order=len(new_node.children)
            if order>len(self.roots):
                self.roots+=[None]*(3+order-len(self.roots))
            for i in self.roots:
                if i==None:
                    j="N/A"
                else:
                    j=i.key
            self.print_tree_with_connected_nodes()
            if self.roots[order]==None:
                self.roots[order]=new_node
                filled==True
                break
            else:
                new_node = self._merge_heaps(self.roots[order], new_node)
                self.roots[order]=None


    def extract_min(self):
        if not self.roots:
            return None

        # Find and remove the minimum value (root node) from the root list
        
        min_node = self.min
        self.roots[len(min_node.children)]=None
        # Extract children into a separate list
        children_list = min_node.children
        min_node.children = []

        # Add children back into the main root list in ascending order of their order
        for child in children_list:
            self.add_value(child)

        return min_node.key
        

    def _merge_heaps(self, node1, node2):
        if node1.key > node2.key:
            node1, node2 = node2, node1

        node1.children.append(node2)
        node2.parent = node1
        return node1

    def print_tree_with_connected_nodes(self):
        visited = set()
        for order, root_node in enumerate(self.roots):
            if root_node is not None and root_node not in visited:
                self.print_connected_nodes(root_node, visited)

    def print_connected_nodes(self, node, visited, indent="", is_last=True):
        if node is None or node in visited:
            return

        visited.add(node)

        children = node.children
        num_children = len(children)

        child_indent = indent + "    "

        for i in range(num_children - 1):
            self.print_connected_nodes(children[i], visited, child_indent, False)

        marker = "└── " if is_last else "├── "
        print(f"{indent}{marker}{node.key}")

        if num_children > 0:
            self.print_connected_nodes(children[num_children - 1], visited, child_indent, True)

# Example usage:
if __name__ == "__main__":
    heap_manager = HeapManager()

    values = [5, 2, 7, 1, 3, 6, 9, 4, 8]

    for value in values:
        heap_manager.insert(value)

    heap_manager.print_tree_with_connected_nodes()
