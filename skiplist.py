from random import randint, seed

class Node:  
    def __init__(self, height=0, value=None):
        self.value = value
        self.next = [None] * height

class SkipList:

    def __init__(self):
        self.head = Node()
        self.length = 0
        self.maxHeight = 0

    def __len__(self):
        return self.length

    def search(self, value, update=None):
        if update is None:
            update = self.updateList(value)
        if len(update) > 0:
            node = update[0].next[0]
            if node is not None and node.value == value:
                return node
        return None
    
    def contains(self, value, update=None):
        return self.search(value, update) is not None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, value):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] is not None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x
        return update
        
    def insert(self, value):
        new_node = Node(self.randomHeight(), value)

        self.maxHeight = max(self.maxHeight, len(new_node.next))
        while len(self.head.next) < len(new_node.next):
            self.head.next.append(None)

        update = self.updateList(value)            
        if self.search(value, update) is None:
            for i in range(len(new_node.next)):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node
            self.length += 1

    def remove(self, value):
        update = self.updateList(value)
        node = self.search(value, update)
        if node is not None:
            for i in reversed(range(len(node.next))):
                update[i].next[i] = node.next[i]
                if self.head.next[i] is None:
                    self.maxHeight -= 1
            self.length -= 1            
                
    def printList(self):
        for i in range(len(self.head.next) - 1, -1, -1):
            x = self.head
            while x.next[i] is not None:
                print(x.next[i].value, end=" ")
                x = x.next[i]
            print('')
skip_list = SkipList()

skip_list.insert(10)
skip_list.insert(5)
skip_list.insert(15)
skip_list.insert(8)
skip_list.insert(12)
skip_list.insert(100)
skip_list.insert(60)
skip_list.insert(120)
skip_list.insert(70)
skip_list.insert(190)
skip_list.insert(40)
skip_list.printList()
print(skip_list.contains(8))


print(skip_list.contains(20))
skip_list.remove(8)
skip_list.remove(15)
skip_list.printList()
print(len(skip_list))

