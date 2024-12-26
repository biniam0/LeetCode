class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = b.zfill(len(a))
        elif len(b) > len(a):
            a = a.zfill(len(b))

        carry, res = 0, ""

        i, j = len(a)-1, len(b)-1
        while i >= 0 and j >= 0:
            if (a[i] == "0" and b[j] == "1") or (a[i] == "1" and b[j] == "0"):
                if carry == 0:
                    res += "1"
                else:
                    res += "0"
                    carry = 1
            elif (a[i] == "1" and b[j] == "1"):
                if carry == 1:
                    res += "1"
                    carry = 1
                else:
                    res += "0"
                    carry = 1
            elif (a[i] == "0" and b[j] == "0"):
                if carry == 1:
                    res += "1"
                    carry = 0
                else:
                    res += "0"

            i -= 1
            j -= 1
        res = "".join(reversed(list(res)))
        return "1" + res if carry == 1 else res