#Binary Search 

'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
'''

'''
Notes:
- We can frame this as a binary search problem -> use true or false rather than a target
- k can be any number between 1 and max(piles) -> we can use binary search to find what the right k is
- Time complexity: O(n log(max_piles))
- Space complexity: O(1)
'''

def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_works(num):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h 

        left = 0
        right = max(piles) 
        while left < right:
            k = (left+right)//2
            if k_works(k):
                right = k 
            else: 
                left = k + 1
        return left

