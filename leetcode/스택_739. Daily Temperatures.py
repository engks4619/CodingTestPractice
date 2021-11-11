from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        answer = [0] * len(temperatures)
        for idx, temperature in enumerate(temperatures):
            while st and temperature > temperatures[st[-1]]:
                last = st.pop()
                answer[last] = idx - last
            st.append(idx)
        return answer