from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        print(counts.most_common(1)[0][0])
        return counts.most_common(1)
Solution.mostCommonWord("self", "Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])