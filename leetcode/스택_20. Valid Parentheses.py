class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")" : "(", "]" : "[", "}" : "{"}
        st = []
        for c in s:
            if c not in dict:
                st.append(c)
            else:
                if not st or st.pop() != dict[c]:
                    return False
        return True if len(st) == 0 else False