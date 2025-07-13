'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

'''
Notes: 
- keep a dictionary where key is element and value is the number of times it appears nums
- keep a frequency list where freq_list[i] is a list of elements that occur i times in nums
    - use the dictionary to fill the frequency list
'''

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq_list = [[] for i in range(len(nums)+1)]
        output = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq_list[c].append(n)

        for i in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[i]:
                output.append(n)

                if len(output) == k: 
                    return output