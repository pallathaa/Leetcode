# Hash maps and sets 

'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

'''
Notes: 
- Break problem into three parts
    - check for duplicates in ROWS
    - check for duplicates in COLUMNS
    - check for duplicates in SUB-BOXES
- Time complexity: O(n^2) - since we know the box is 9*9, complexity ends up being O(1)
- Space complexity: O(n) - becomes O(1) using same logic as above
'''

def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # validate rows 
        for i in range(9):
            seen = set()
            for j in range(9):
                curr_elem = board[i][j]
                if curr_elem in seen: 
                    return False
                elif curr_elem != '.':
                    seen.add(curr_elem)

        # validate columns
        for i in range(9):
            seen = set()
            for j in range(9):
                curr_elem = board[j][i]
                if curr_elem in seen: 
                    return False
                elif curr_elem != '.':
                    seen.add(curr_elem)

        # validate sub-boxes

        starts = [(0,0), (0,3), (0,6), 
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]
        
        for i,j in starts:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    curr_elem = board[row][col]
                    if curr_elem in seen: 
                        return False
                    elif curr_elem != '.':
                        seen.add(curr_elem)
        return True