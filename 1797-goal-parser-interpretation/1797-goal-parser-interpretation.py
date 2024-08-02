class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = ""
        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            elif command[i] == "(" and command[i+1] == ")":
                result += "o"
                i += 2
            elif command[i] == "(" and command[i+1] == "a":
                result += "al"
                i += 4

        return result