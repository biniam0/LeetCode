class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        tmp = ""

        for char in command:
            if tmp == "G":
                res += "G"
                tmp = ""
            elif tmp == "()":
                res += "o"
                tmp = ""
            elif tmp == "(al)":
                res += "al"
                tmp = ""
            tmp += char

        if tmp == "G":
            res += "G"
        elif tmp == "()":
            res += "o"
        elif tmp == "(al)":
            res += "al"
        return res