class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_cnt = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill ==  10:
                if bills_cnt[5] >= 1:
                    bills_cnt[5] -= 1
                    bills_cnt[bill] += 1
                else:
                    return False
            elif bill == 20:
                if bills_cnt[10] >= 1 and bills_cnt[5] >= 1:
                    bills_cnt[10] -= 1
                    bills_cnt[5] -= 1
                elif bills_cnt[5] >= 3:
                    bills_cnt[5] -= 3
                else:
                    return False
            else:
                bills_cnt[5] += 1
                
        return True
            
