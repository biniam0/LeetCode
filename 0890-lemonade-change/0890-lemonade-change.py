class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills = []
        ten_bills = []
        twenty_bills = []
        for i in range(len(bills)):
            if bills[i] == 5:
                five_bills.append(bills[i])
                continue
            if bills[i] == 10 and five_bills:
                ten_bills.append(bills[i])
                five_bills.pop()
            elif bills[i] == 20 and five_bills and ten_bills:
                twenty_bills.append(bills[i])
                ten_bills.pop()
                five_bills.pop()
            elif bills[i] == 20 and len(five_bills) >= 3:
                twenty_bills.append(bills[i])
                for i in range(3):
                    five_bills.pop()
            elif i == len(bills) - 1:
                return False
            else:
                return False

        return True