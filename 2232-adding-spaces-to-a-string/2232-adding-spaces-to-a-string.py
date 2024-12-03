class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        stack = []
        i = 0
        for idx in spaces:
            stack.append(s[i:idx] + " ")
            i = idx

        return "".join(stack) + s[i:]

        # s_list = list(s)
        # for sp in reversed(spaces):
        #     s_list.insert(sp, " ")

        # return "".join(s_list)
