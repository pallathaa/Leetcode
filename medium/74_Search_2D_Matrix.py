# Binary Search
'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

'''
Notes:
- treat the matrix as if it was a flattened array (indexed based on order of integers)
- Row index can be obtained by dividing middle index by number of columns (integer division)
- Column index can be obtained by doing middle index % number of columns
- Time complexity: O(log mn)
- Space complexity: O(1)
'''

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        left = 0
        right = t-1

        while left <= right:
            mid = (left + right)//2
            row = mid // n
            col = mid % n
            elem = matrix[row][col]
            if elem > target:
                right = mid - 1
            if elem < target:
                left = mid + 1
            if elem == target:
                return True
        
        else: 
            return False 