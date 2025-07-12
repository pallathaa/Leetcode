'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

'''
Notes: Keep track of boundaries and update them as we go along
Time complexity: O(mn)
Space complexity: O(1) if we don't include answer, O(mn) if we do include answer
'''

def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(matrix), len(matrix[0])
        answer = []
        i, j = 0, 0
        UP, DOWN, LEFT, RIGHT =  0, 1, 2, 3  
        direction = RIGHT   
        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(answer) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    answer.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
            
            elif direction == DOWN:
                while i < DOWN_WALL:
                    answer.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                DOWN_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    answer.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP
            
            else: 
                while i > UP_WALL:
                    answer.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                UP_WALL += 1
                direction = RIGHT

        return answer

