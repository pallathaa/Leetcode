# Two Pointers

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

'''
Notes for solution 1:
- All you need to know is max height to the left, max height to the right
    - Can store both of these things in an array 
    - Max_left 
    - Max_right
    - Trapped_water[i] = min(Max_right[i], Max_left[i]) - height[i]
- Time Complexity: O(n)
- Space Complexity: O(n)
'''

def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        left_wall = 0
        right_wall = 0

        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            max_right[j] = right_wall 
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])

        total_water = 0
        for i in range(n):
            trapped_water = min(max_left[i], max_right[i]) - height[i]
            total_water += max(0, trapped_water)
        
        return total_water

'''
Notes for solution 2:
- Two pointer solution -> left pointer and right pointer 
    - keep track of max left seen so far and max right seen so far 
    - move left pointer if max left is less then max right 
- Time Complexity: O(n)
- Space Complexity: O(1)
'''

# Solution 2
def trap(self, height):
    n = len(height)
    if not height: return 0
    left_ptr, right_ptr = 0, n-1
    left_max, right_max = height[left_ptr], height[right_ptr]
    total_water = 0 

    # keep going until the two pointers meet
    while left_ptr < right_ptr: 
        # if max left seen so far < max right seen so far, move left pointer 
        if left_max < right_max: 
            left_ptr += 1
            total_water += max(0, left_max - height[left_ptr])
            left_max = max(left_max, height[left_ptr])
             
        # else move right pointer
        else: 
            right_ptr -=1
            total_water += max(0, right_max - height[right_ptr])
            right_max = max(right_max, height[right_ptr])
    return total_water
         



