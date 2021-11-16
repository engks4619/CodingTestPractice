#해시 테이블
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = {}

        for char in stones:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1

        result = 0
        for char in jewels:
            if char in table:
                result += table[char]

        return result

#defaultdict
from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = defaultdict(int)

        for char in stones:
            table[char] += 1

        result = 0
        for char in jewels:
            result += table[char]

        return result

#Counter
from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        result = 0
        for char in jewels:
            result += counter[char]
        
        return result

#파이썬다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)