class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt_to_domains = defaultdict(int)
        ans = []

        for i in range(len(cpdomains)):
            cnt, *domain = cpdomains[i].split()
            domains = domain[0].split(".")

            for i in range(len(domains)-1, -1, -1):
                each_dmn = ".".join(domains[i:])
                cnt_to_domains[each_dmn] += int(cnt)

        for dmn, freq in cnt_to_domains.items():
            ans.append(f"{freq} {dmn}")

        return ans
