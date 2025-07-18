# hash map 

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''


'''
Notes:
- We want to keep track of capacity
- we want a hashmap where the keys are the int keys provided as input and values are pointers to nodes containing key value pairs 
- we keep a doubly linked list with two pointers(left, right)
- left points toward least recently used 
- right points towards most recently used 
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node 

        self.left = Node(0,0) # least recently used 
        self.right = Node(0,0) # most recently used 
        self.left.next, self.right.prev = self.right, self.left

    def insert_right(self, node):
        old_mru = self.right.prev
        self.right.prev = node 
        node.next = self.right
        node.prev = old_mru
        old_mru.next = node
    
    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next, nex.prev = nex, prev


    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert_right(new_node)

        if len(self.cache.keys()) > self.capacity: 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

            


        

    

