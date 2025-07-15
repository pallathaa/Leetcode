'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

'''
Notes: 
- Time complexity: O(n)
- Space complexity: O(n)
'''

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        output = []
        
        while q: 
            n = len(q)
            summ = 0
            for i in range(n):
                node = q.popleft()
                summ += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(summ/n)
        return output