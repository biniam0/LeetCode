class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        temp_dict = defaultdict(list)

        for p in paths:
            path = p.split()

            for i in range(1, len(path)):
                con_path = path[i].split("(")

                temp_dict[con_path[-1]].append(path[0] + "/" + con_path[0])

        for path in temp_dict.values():
            if len(path) >= 2:
                ans.append(path)
        return ans