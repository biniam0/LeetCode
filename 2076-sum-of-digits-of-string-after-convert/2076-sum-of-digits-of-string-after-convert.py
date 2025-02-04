class Solution:
    def getLucky(self, s: str, k: int) -> int:
        str_ = ""

        for char in s:
            str_ += f"{ord(char) - 96}"

        ans = str_
        for _ in range(k):
            tmp = sum(list(map(int, ans)))
            ans = str(tmp)

        return int(ans)

