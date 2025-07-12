'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

'''
Notes for solution 1: 
- Break the problem down into two steps
    1) transpose the matrix -> reflection along the diagonal (swap i,j with j,i where i!=j)
    2) Reflect Vertically along the middle column (Called Horizontal Reflection)
- Time complexity: O(n^2)
- Space complexity: O(1)
'''

# Solution 1
def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Transpose 
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflect
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j] 


'''
Notes for solution 2: 
- Performs the rotation layer by layer
- Swaps 4 elements at a time
- Avoids the separate transpose and reflect steps

Each element at (row, col) moves to (col, n - 1 - row)

So for each layer, you rotate:
top   -> right
right -> bottom
bottom -> left
left -> top

- Time complexity: O(n^2)
- Space complexity: O(1)
- Advantage: Slightly fewer writes, better cache locality, faster in practice for large matrices
'''

# Solution 2
def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None. Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
