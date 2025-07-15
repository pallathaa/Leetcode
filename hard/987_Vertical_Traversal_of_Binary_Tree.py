'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.


Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.


Example 3:

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Notes for solution 1: 
- Time complexity: O(nlogn)
- Space complexity: O(n)
'''

# Solution 1
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, (0, 0)))
        nodes = []

        while q: 
            node, row, col = q.popleft()
            nodes.append(col, row, node.val)
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        nodes.sort()
        res = defaultdict(list)
        for col,row,node in nodes:
            res[col].append(node)
        return [res[col] for col in sorted(res)]  
    
'''
Notes: 
- Time complexity: O(n log(n/c))
- Space complexity: O(n)
'''

from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Step 1: BFS and group by column
        col_map = defaultdict(list)
        queue = deque([(root, 0, 0)])  # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            if node:
                col_map[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        # Step 2: Sort each column's list by (row, val)
        result = []
        for col in sorted(col_map.keys()):  # left to right
            col_entries = sorted(col_map[col])  # sort small sublists
            result.append([val for row, val in col_entries])

        return result
