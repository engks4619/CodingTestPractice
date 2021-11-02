from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        print(anagrams.values())
        return list(anagrams.values())

Solution.groupAnagrams("self", ["eat","tea","tan","ate","nat","bat"])        