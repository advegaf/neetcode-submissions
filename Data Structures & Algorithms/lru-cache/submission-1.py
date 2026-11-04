class Node: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to the nodes (val)
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

        #left lru
        #right most recently used

    #manipulate pointers w/ helper functions:
    def remove(self, node):
        #remove node from the list 
        # node will be the middle node so we need previous and next node to connect our list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        # insert at rightmost position right before our right pointer 
        # say that our right pointer is b and our previous pointer is a 
        # [a] <-C-> [b] we want to insert at C so we need to point a's next to C and b's prev to C, and C's next to b and C's prev to a 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node # both now point to node 
        node.next, node.prev = nxt, prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to update the most recent:
            # since we are getting we want to remove it from our list and then add it at the right most position of the list since it was the most recently used, and in that case we can always know that our most recent lives in the far right corner of the list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
             #tells us the actual node so we just need the value with .val
        return -1 # in the case it doesn't exists


    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            # if it already exists we can just replace by first removing and then adding it again 
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove/evict the LRU which is the left pointer:
            # remove from the linked list, and delete it from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key] # we keep the actual key in our node 

