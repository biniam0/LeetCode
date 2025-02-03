class Solution:
    def maskPII(self, s: str) -> str:
        ans = ""
        if "@" in s:
            fst, sec = s.split("@")
            s, e = fst[0], fst[-1]
            ans += s.lower()
            ans += "*****"
            ans += e.lower() + "@"
            ans += sec.lower()
        else:
            num = ""
            for n in s:
                if n not in {'+', '-', '(', ')', ' '}:
                    num += n
            print(num)

            last_dig = num[-4:]
            code = ""
            if len(num) == 10:
                ans += "***-***-" + last_dig
            elif len(num) == 11:
                ans += "+*-***-***-" + last_dig
            elif len(num) == 12:
                ans += "+**-***-***-" + last_dig
            else:
                ans += "+***-***-***-" + last_dig

        return ans