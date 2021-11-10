'''
# 재귀
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

answer = Solution().removeDuplicateLetters("cbacdcbc")
print(answer)

'''
# 스택
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        st = []
        seen = set()
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while st and char < st[-1] and counter[st[-1]] > 0:
                seen.remove(st.pop())
            st.append(char)
            seen.add(char)

        return "".join(st)