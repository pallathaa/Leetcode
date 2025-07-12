'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

'''
Notes:
- One option would be to sort all words and then check if they're equal: O(nmlogm) time complexity
- Instead, we calculate frequency dictionary of every words and check if the dictionaries are the same
    - we can then make a list of all words that have the same frequency dictionary 
    - dictionaries can't be used as keys though because they are mutable and not hashable
    - so, instead of using dictionaries we use arrays, converted into tuples

- Time complexity: O(nm)
- Space complexity: O(nm)
'''

from collections import defaultdict

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s: 
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        
        return anagrams_dict.values()


