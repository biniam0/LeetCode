class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def buildTheBit(n):
            s_1 = "0"
            for i in range(n):
                list_s = list(s_1)

                # For inverting the string
                for i in range(len(list_s)):
                    if list_s[i] == "1":
                        list_s[i] = "0"
                    else:
                        list_s[i] = "1"

                s_1 = s_1 + "1" + "".join(reversed(list_s))

            return s_1

        s_n = buildTheBit(n)

        return s_n[k-1]