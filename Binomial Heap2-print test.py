class HeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

class HeapManager:
    def __init__(self):
        self.roots = [None]*10
        self.min=HeapNode(float('inf'))

    def insert(self,key):
        new_node = HeapNode(key)
        self.add_value(new_node) 
    def add_value(self, _node):
        new_node = _node
        if new_node.key<self.min.key:
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

        
        min_node = self.min
        self.roots[len(min_node.children)]=None
        children_list = min_node.children
        min_node.children = []
        for child in children_list:
            self.add_value(child)
            
        
        self.find_min()
        return min_node.key
        
    def find_min(self):
        minval=HeapNode(float('inf'))
        for i in self.roots:
            if i != None:
                if i.key<minval.key:
                    minval=i
            self.min=minval

    def find_node(self, key):
        return self._search_key_recursive(self.min, key)

    def _search_key_recursive(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node

        for child in node.children:
            found_node = self._search_key_recursive(child, key)
            if found_node is not None:
                return found_node

        return None

    def reduce_key(self, key,new_key):
        if new_key > key:
            raise ValueError("New value is greater than current value")
        node=self.find_node(key)
        node.key=new_key
        parent = node.parent
        while parent is not None and node.key < parent.key:
            parent = node.parent
            if parent != None:
                node.key, parent.key = parent.key, node.key
                node, parent = parent, node

    
    def delete_key(self, key):
        node=self.reduce_key(key,-100)
        self.extract_min()


    def delete_node(self,node):
        
        for child in node.children:
            self.add_value(child)
        
        
            
        




    def _merge_heaps(self, node1, node2):
        if node1.key > node2.key:
            node1, node2 = node2, node1

        node1.children.append(node2)
        node2.parent = node1
        return node1

    
    def print_tree(self):
        visited = set()
        for order in range(len(self.roots) - 1, -1, -1):  # Traverse in reverse order
            root_node = self.roots[order]
            if root_node is not None and root_node not in visited:
                self.print_connected_nodes(root_node, visited)

    def print_connected_nodes(self, node, visited, indent="", is_last=True):
        if node is None or node in visited:
            return

        visited.add(node)

        children = node.children
        num_children = len(children)

        child_indent = indent + "    "

        for i in range(num_children - 1, -1, -1):  # Traverse in reverse order
            self.print_connected_nodes(children[i], visited, child_indent, i == num_children - 1)

        marker = "┌──  " if is_last else "├── "
        print(f"{indent}{marker}{node.key}")

# Example usage:
if __name__ == "__main__":
    hm = HeapManager()

    values = [2,3,4,5,6,9,70,50,33,44]

    for value in values:
        hm.insert(value)

    hm.print_tree()
