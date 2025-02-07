class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_freq = defaultdict(int)
        ball_to_color = defaultdict(int)
        ans = []

        for q in queries:
            ball, color = q

            clr = ""
            if ball in ball_to_color:
                prev_clr = ball_to_color[ball]
                color_freq[prev_clr] -= 1
                if color_freq[prev_clr] == 0 :
                    del color_freq[prev_clr]
        
            ball_to_color[ball] = color
            color_freq[color] += 1
            
            ans.append(len(color_freq))
        
        return ans