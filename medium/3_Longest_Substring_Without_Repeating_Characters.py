# Sliding window
'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
Notes:
- left pointer and right pointer 
- we want to keep track of current substring using a set
- while the right pointer element is within the set, remove the left pointer element and increment left pointer 
- add the right pointer element in set once it's duplicate is removed 
- keep moving the right pointer all the way to the end 
- keep tracking the longest seen so far

- Time complexity: O(n)
- Space complexity: O(n)

'''

def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    longest = 0
    elems = set()
    n = len(s)

    for right in range(n):
        while s[right] in elems:
            elems.remove(s[left])
            left += 1
        len_window = (right-left) + 1
        longest = max(longest, len_window)
        elems.add(s[right])
    return longest