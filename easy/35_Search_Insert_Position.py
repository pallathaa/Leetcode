# Binary Search: O(log n) runtime complexity
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

'''
Notes:
- Time complexity: O(log n)
- Space complexity: O(1)
'''

def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left_ptr = 0
        right_ptr = n-1
        
        while left_ptr <= right_ptr: 
            middle_ptr = (right_ptr + left_ptr)//2

            if nums[middle_ptr] < target:
                left_ptr = middle_ptr + 1
            
            elif nums[middle_ptr] > target:
                right_ptr = middle_ptr - 1
            
            else:
                return middle_ptr
        
        if nums[middle_ptr] < target: 
            return middle_ptr + 1

        if nums[middle_ptr] > target:
            return middle_ptr

