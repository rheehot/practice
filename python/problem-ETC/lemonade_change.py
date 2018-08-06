#   https://leetcode.com/problems/lemonade-change

#   https://leetcode.com/problems/lemonade-change/solution


class Solution:
    #   Wrong Answer
    def lemonadeChange0(self, bills):
        if bills is None or 0 == len(bills):
            return True
        inDict, outDict1, outDict2 = {5:0, 10:0}, {5:0, 10:0}, {5:0, 10:0}
        for bill in bills:
            if 5 == bill:
                inDict[5] +=1
            elif 10 == bill:
                inDict[10] += 1
                outDict1[5] += 1
                outDict2[5] += 1
            elif 20 == bill:
                outDict1[5] += 3
                outDict2[5] += 1
                outDict2[10] += 1
        return (inDict[5] >= outDict1[5] and inDict[10] >= outDict1[10]) or  (inDict[5] >= outDict2[5] and inDict[10] >= outDict2[10])

    #   Time Limit Exceeded
    def lemonadeChange1(self, bills):
        if bills is None or 0 == len(bills):
            return True
        def _lemonadeChange(numFives, numTens, left):
            if numFives < 0 or numTens < 0:
                return False
            if 0 == len(left):
                return True
            if 5 == left[0]:
                return _lemonadeChange(numFives + 1, numTens, left[1:])
            if 10 == left[0]:
                return _lemonadeChange(numFives - 1, numTens + 1, left[1:])
            return _lemonadeChange(numFives - 3, numTens, left[1:]) or _lemonadeChange(numFives - 1, numTens - 1, left[1:])
        return _lemonadeChange(0, 0, bills)

    #   95.68%
    def lemonadeChange(self, bills):
        if bills is None or 0 == len(bills):
            return True
        fives, tens = 0, 0
        for bill in bills:
            if 5 == bill:
                fives += 1
            elif 10 == bill:
                tens += 1
                if fives < 1:
                    return False
                fives -= 1
            elif 20 == bill:
                if 0 < tens and 0 < fives:
                    tens -= 1
                    fives -= 1
                elif 3 < fives:
                    fives -= 3
                else:
                    return False
        return True


s = Solution()
data = [([5, 5, 5, 10, 20], True),
        ([5, 5, 10], True),
        ([10, 10], False),
        ([5, 5, 10, 10, 20], False),
        ([5, 5, 5, 5, 20, 20, 5, 5, 5, 5], False),
        ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 20, 5, 20, 5, 20, 10, 5, 5, 20, 20, 5, 5, 5, 10, 5, 5, 10, 5, 10, 10, 5, 20, 10, 5, 5, 20, 20, 5, 20, 10, 10, 10, 5, 20, 10, 5, 20, 10, 20, 5, 20, 5, 5, 5, 5, 10, 20, 5, 10, 20, 5, 5, 5, 5, 10, 20, 5, 5, 5, 20, 5, 5, 20, 5, 20, 10, 20, 10, 5, 10, 5, 10, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 20, 10, 20, 5, 5, 5, 5, 5, 10, 20, 5, 5, 20, 5, 5, 20, 5, 5, 10, 5, 20, 10, 20, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 20, 5, 20, 20, 20, 5, 20, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 10, 5, 5, 10, 5, 10, 5, 20, 5, 20, 10, 5, 20, 5, 5, 5, 5, 10, 5, 10, 5, 5, 20, 5, 20, 20, 20, 20, 20, 5, 20, 20, 5, 10, 5, 10, 20, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 10, 10, 20, 10, 10, 5, 5, 10, 20, 5, 20, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 20, 10, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 5, 20, 10, 20, 5, 5, 10, 20, 5, 5, 5, 20, 5, 20, 5, 5, 20, 10, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 5, 10, 5, 5, 10, 5, 10, 5, 5, 20, 5, 20, 5, 20, 10, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 20, 5, 10, 20, 5, 20, 5, 5, 5, 20, 5, 5, 5, 10, 20, 10, 10, 20, 10, 10, 5, 5, 20, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 20, 20, 5, 10, 5, 5, 10, 5, 5, 20, 20, 20, 5, 10, 10, 20, 10, 20, 5, 10, 10, 10, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 20, 5, 5, 10, 5, 5, 20, 5, 10, 5, 5, 10, 20, 20, 10, 5, 5, 20, 5, 20, 5, 5, 5, 5, 10, 20, 5, 20, 5, 10, 20, 5, 10, 5, 10, 10, 20, 5, 5, 10, 5, 5, 20, 20, 10, 10, 5, 5, 10, 20, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 5, 20, 10, 20, 5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 10, 5, 20, 5, 5, 5, 20, 5, 5, 10, 20, 10, 5, 20, 5, 10, 5, 5, 10, 20, 20, 10, 5, 20, 10, 5, 20, 5, 20, 5, 5, 20, 10, 10, 10, 20, 5, 10, 5, 5, 5, 20, 5, 5, 20, 20, 5, 20, 5, 10, 20, 5, 10, 20, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 20, 20, 5, 20, 10, 10, 5, 10, 5, 10, 20, 5, 5, 10, 5, 5, 10, 5, 10, 5, 5, 5, 10, 5, 5, 5, 10, 5, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 10, 20, 10, 5, 5, 20, 5, 20, 5, 5, 5, 5, 20, 10, 5, 20, 5, 10, 5, 20, 5, 20, 5, 5, 10, 5, 20, 5, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 20, 5, 5, 20, 10, 5, 10, 10, 10, 20, 5, 5, 10, 5, 20, 10, 5, 10, 10, 5, 20, 20, 5, 5, 5, 10, 5, 5, 5, 20, 10, 5, 5, 20, 5, 5, 5, 20, 10, 5, 5, 10, 20, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 20, 10, 5, 5, 20, 20, 5, 10, 5, 5, 5, 20, 10, 20, 5, 10, 20, 10, 10, 5, 20, 5, 5, 20, 5, 5, 10, 5, 20, 10, 20, 10, 5, 20, 5, 20, 5, 20, 5, 5, 5, 20, 20, 20, 5, 20, 5, 5, 20, 5, 10, 5, 5, 10, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 20, 10, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 10, 5, 10, 5, 5, 5, 10, 5, 20, 10, 20, 5, 5, 5, 10, 20, 5, 20, 10, 10, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 20, 5, 20, 5, 5, 10, 10, 10, 5, 10, 5, 10, 20, 5, 5, 20, 5, 20, 5, 5, 10, 5, 5, 10, 5, 5, 20, 10, 5, 20, 5, 20, 20, 10, 20, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 20, 20, 20, 10, 20, 20, 5, 10, 5, 5, 20, 5, 5, 20, 5, 5, 20, 5, 5, 10, 5, 5, 5, 10, 20, 5, 5, 20, 10, 20, 10, 10, 20, 5, 5, 10, 5, 5, 5, 10, 5, 5, 10, 5, 20, 5, 10, 5, 10, 5, 5, 5, 5, 5, 20, 10, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 10, 20, 20, 20, 5, 5, 20, 5, 5, 5, 5, 20, 5, 20, 20, 20, 5, 20, 5, 5, 20, 5, 20, 5, 5, 10, 5, 10, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 10, 5, 5, 5, 20, 10, 10, 5, 5, 10, 10, 5, 20, 10, 5, 20, 5, 5, 5, 5, 20, 20, 10, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 20, 5, 20, 20, 10, 20, 5, 5, 20, 5, 10, 10, 5, 20, 20, 5, 5, 5, 5, 20, 5, 5, 10, 10, 10, 5, 20, 5, 5, 10, 20, 10, 5, 5, 20, 5, 20, 20, 5, 10, 5, 5, 5, 20, 5, 10, 5, 20, 20, 10, 5, 5, 5, 10, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 20, 5, 5, 10, 20, 10, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 10, 20, 5, 20, 5, 10, 5, 20, 5, 5, 20, 20, 5, 10, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 20, 5, 20, 10, 5, 5, 5, 5, 20, 10, 5, 10, 5, 10, 5, 20, 5, 20, 10, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 10, 5, 20, 5, 5, 10, 5, 20, 20, 10, 10, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 20, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 20, 5, 10, 5, 20, 5, 5, 5, 5, 20, 5, 10, 10, 5, 20, 5, 5, 10, 5, 20, 10, 5, 20, 5, 20, 5, 5, 5, 20, 10, 20, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 10, 20, 5, 5, 10, 5, 20, 20, 20, 5, 10, 5, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 10, 5, 5, 10, 10, 5, 5, 5, 20, 5, 10, 10, 5, 5, 20, 5, 5, 5, 10, 20, 20, 5, 5, 5, 5, 5, 5, 20, 10, 5, 20, 10, 5, 20, 5, 20, 10, 20, 20, 10, 20, 5, 20, 10, 5, 10, 20, 20, 10, 5, 5, 10, 20, 5, 5, 5, 20, 5, 5, 10, 5, 10, 5, 10, 5, 10, 10, 20, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 20, 5, 20, 20, 20, 5, 5, 5, 10, 5, 20, 20, 20, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 10, 10, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 10, 20, 10, 20, 5, 20, 5, 20, 5, 20, 10, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 20, 5, 20, 20, 5, 20, 5, 5, 5, 5, 10, 20, 5, 5, 20, 10, 5, 5, 20, 5, 20, 10, 5, 5, 20, 10, 10, 20, 5, 5, 10, 10, 20, 5, 20, 5, 10, 20, 10, 5, 5, 10, 5, 10, 5, 5, 20, 5, 5, 5, 5, 10, 5, 20, 20, 5, 20, 5, 5, 10, 10, 5, 5, 5, 10, 10, 20, 5, 10, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 10, 5, 10, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 20, 20, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 10, 20, 20, 5, 5, 20, 10, 5, 5, 5, 5, 5, 10, 5, 10, 20, 10, 10, 5, 5, 5, 5, 20, 10, 10, 5, 20, 5, 10, 5, 10, 5, 10, 5, 5, 20, 5, 5, 5, 10, 10, 5, 5, 20, 5, 5, 10, 20, 5, 20, 5, 10, 10, 5, 20, 5, 5, 20, 5, 5, 5, 5, 20, 20, 5, 20, 10, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 20, 10, 5, 10, 5, 10, 20, 20, 20, 5, 5, 10, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 10, 10, 20, 10, 5, 5, 10, 10, 5, 10, 20, 10, 5, 5, 5, 5, 10, 10, 10, 5, 5, 20, 5, 5, 5, 5, 10, 5, 20, 5, 20, 5, 20, 10, 5, 10, 20, 5, 10, 5, 5, 5, 10, 5, 10, 5, 10, 5, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 20, 10, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 10, 10, 5, 5, 5, 10, 5, 10, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 10, 5, 5, 10, 10, 20, 10, 20, 10, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 10, 20, 20, 5, 5, 5, 10, 5, 20, 20, 5, 10, 5, 5, 20, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 20, 20, 10, 20, 5, 5, 5, 5, 20, 5, 10, 10, 10, 20, 10, 10, 20, 10, 20, 5, 5, 20, 20, 5, 5, 5, 5, 5, 10, 20, 10, 5, 10, 5, 5, 20, 5, 5, 20, 5, 10, 5, 20, 20, 5, 20, 5, 10, 5, 5, 10, 5, 10, 5, 5, 5, 10, 20, 10, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 5, 5, 5, 10, 5, 5, 10, 5, 20, 5, 5, 20, 20, 5, 5, 5, 5, 20, 5, 5, 10, 20, 10, 5, 5, 5, 5, 5, 20, 20, 5, 20, 10, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 10, 5, 10, 20, 5, 10, 20, 10, 10, 5, 5, 5, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 20, 5, 20, 20, 5, 5, 5, 5, 5, 20, 20, 20, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 5, 5, 10, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 20, 20, 5, 20, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 20, 10, 20, 5, 5, 10, 10, 5, 20, 20, 5, 10, 5, 5, 10, 10, 10, 5, 10, 5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 10, 10, 5, 5, 5, 5, 5, 20, 20, 20, 5, 20, 5, 10, 5, 20, 10, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 20, 20, 20, 5, 20, 5, 5, 10, 5, 10, 5, 10, 20, 5, 20, 5, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 20, 5, 5, 5, 5, 5, 10, 20, 5, 20, 5, 5, 20, 5, 5, 5, 5, 5, 20, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 10, 5, 10, 20, 5, 20, 10, 20, 10, 5, 5, 10, 5, 5, 10, 10, 10, 5, 5, 5, 20, 10, 5, 20, 20, 20, 20, 20, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 5, 5, 20, 5, 20, 20, 5, 10, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 20, 20, 5, 5, 20, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 20, 20, 5, 20, 5, 5, 5, 20, 20, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 5, 5, 10, 20, 5, 5, 20, 5, 20, 10, 20, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 10, 5, 20, 5, 5, 5, 5, 10, 10, 20, 10, 5, 10, 5, 20, 10, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 20, 5, 20, 10, 5, 10, 10, 20, 5, 5, 10, 20, 5, 10, 10, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 20, 20, 5, 5, 5, 10, 10, 20, 10, 5, 20, 10, 5, 20, 10, 10, 5, 20, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 20, 5, 20, 5, 5, 10, 5, 10, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 10, 10, 5, 20, 10, 20, 20, 20, 5, 5, 5, 5, 5, 10, 5, 20, 20, 5, 5, 5, 20, 20, 5, 5, 20, 5, 5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 20, 5, 10, 5, 5, 5, 20, 5, 5, 5, 20, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 5, 5, 20, 10, 20, 5, 5, 10, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 10, 20, 5, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 20, 5, 5, 10, 5, 5, 20, 10, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 10, 5, 10, 20, 10, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 10, 20, 5, 20, 5, 5, 5, 5, 5, 5, 20, 5, 10, 10, 5, 20, 5, 20, 20, 20, 10, 5, 5, 10, 5, 20, 20, 5, 20, 5, 10, 5, 5, 5, 10, 20, 20, 10, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 5, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 20, 5, 5, 5, 5, 5, 20, 10, 5, 5, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20, 10, 5, 20, 5, 20, 5, 5, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5, 10, 20, 5, 10, 5, 10, 20, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 10, 20, 5, 5, 20, 10, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 20, 5, 20, 20, 20, 5, 10, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 20, 20, 10, 5, 10, 5, 5, 10, 5, 20, 5, 10, 5, 5, 5, 5, 10, 20, 10, 20, 5, 5, 20, 5, 5, 20, 5, 5, 10, 20, 20, 5, 10, 5, 20, 10, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 5, 20, 5, 20, 20, 5, 5, 5, 10, 5, 20, 5, 5, 20, 10, 5, 20, 5, 20, 5, 20, 10, 10, 20, 20, 5, 5, 20, 10, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 10, 5, 20, 20, 5, 5, 10, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 10, 10, 10, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 10, 5, 20, 20, 5, 5, 5, 5, 20, 5, 20, 10, 5, 5, 20, 10, 5, 5, 10, 5, 20, 5, 10, 5, 20, 5, 20, 5, 5, 20, 10, 20, 5, 10, 10, 10, 5, 5, 5, 5, 10, 5, 20, 10, 5, 5, 10, 20, 5, 5, 20, 5, 10, 5, 20, 20, 5, 5, 20, 5, 20, 5, 5, 10, 5, 20, 10, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 10, 5, 10, 5, 20, 10, 5, 10, 20, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 10, 20, 10, 5, 5, 20, 5, 20, 5, 10, 5, 5, 20, 10, 5, 20, 5, 10, 20, 5, 20, 5, 5, 10, 5, 10, 5, 5, 5, 20, 10, 5, 20, 5, 10, 5, 5, 10, 20, 5, 5, 20, 20, 5, 5, 10, 20, 5, 5, 5, 20, 5, 20, 5, 5, 10, 20, 10, 5, 10, 20, 10, 5, 5, 10, 5, 5, 5, 5, 20, 10, 10, 10, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 10, 10, 20, 5, 20, 20, 5, 5, 5, 5, 20, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 20, 10, 20, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 5, 10, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 20, 20, 5, 20, 5, 5, 5, 20, 5, 5, 20, 10, 5, 5, 5, 5, 5, 20, 10, 20, 10, 10, 10, 5, 20, 5, 10, 5, 10, 5, 10, 5, 20, 10, 5, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 20, 20, 5, 5, 10, 10, 10, 5, 10, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 5, 20, 20, 5, 20, 20, 10, 10, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 10, 20, 20, 5, 5, 5, 20, 10, 20, 5, 5, 5, 20, 5, 10, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 20, 10, 5, 10, 5, 5, 10, 5, 5, 10, 10, 10, 10, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 10, 10, 10, 5, 5, 10, 5, 10, 20, 20, 10, 5, 5, 5, 20, 5, 10, 5, 5, 5, 10, 5, 10, 5, 5, 20, 10, 5, 5, 10, 5, 5, 10, 5, 10, 20, 5, 5, 5, 5, 5, 10, 20, 20, 10, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 20, 5, 5, 5, 20, 5, 20, 5, 5, 5, 20, 5, 5, 10, 20, 5, 20, 5, 5, 10, 20, 5, 5, 5, 20, 20, 20, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 20, 5, 5, 5, 20, 5, 20, 20, 5, 5, 20, 10, 5, 20, 5, 20, 20, 5, 20, 10, 10, 5, 5, 5, 20, 20, 5, 5, 20, 10, 5, 5, 5, 20, 5, 10, 20, 20, 5, 5, 10, 20, 20, 10, 5, 5, 5, 20, 5, 5, 5, 5, 20, 5, 10, 5, 20, 20, 5, 20, 20, 20, 5, 5, 10, 5, 5, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 10, 20, 5, 20, 10, 5, 10, 20, 20, 5, 20, 20, 10, 5, 5, 10, 10, 5, 5, 5, 20, 5, 20, 20, 5, 20, 5, 5, 20, 5, 5, 5, 20, 20, 20, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 20, 20, 5, 5, 10, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 20, 5, 10, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 10, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 10, 5, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 20, 20, 5, 10, 5, 5, 5, 5, 5, 5, 10, 20, 20, 5, 20, 10, 10, 5, 10, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 20, 5, 10, 10, 10, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 20, 20, 5, 5, 20, 5, 5, 5, 20, 5, 20, 5, 5, 5, 20, 5, 5, 10, 5, 10, 5, 20, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 5, 20, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 10, 20, 10, 5, 5, 20, 5, 20, 5, 10, 10, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 10, 5, 20, 5, 10, 5, 10, 5, 20, 5, 10, 5, 20, 10, 5, 5, 5, 5, 5, 10, 10, 5, 10, 5, 5, 5, 5, 20, 10, 10, 5, 10, 10, 20, 5, 5, 20, 5, 10, 5, 10, 20, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 20, 10, 5, 10, 5, 10, 5, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 20, 5, 20, 5, 10, 5, 5, 5, 5, 10, 5, 20, 5, 5, 10, 5, 5, 10, 20, 10, 5, 5, 5, 10, 20, 5, 10, 5, 5, 5, 20, 5, 5, 10, 20, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 5, 10, 10, 5, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 20, 20, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 20, 20, 10, 5, 20, 10, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 20, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 10, 20, 5, 20, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 20, 5, 5, 5, 10, 10, 5, 20, 5, 5, 10, 5, 20, 5, 5, 5, 20, 5, 5, 5, 10, 10, 20, 5, 5, 20, 5, 20, 20, 20, 5, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 20, 5, 5, 5, 20, 10, 5, 5, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 20, 10, 10, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 20, 5, 10, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 10, 5, 5, 5, 20, 5, 5, 10, 5, 20, 5, 5, 10, 5, 5, 20, 5, 10, 5, 5, 5, 20, 10, 5, 10, 10, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 5, 10, 20, 5, 20, 20, 10, 5, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 20, 10, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 10, 10, 5, 5, 5, 5, 20, 5, 10, 5, 10, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 20, 5, 20, 5, 5, 5, 20, 5, 5, 20, 5, 20, 10, 20, 10, 5, 5, 5, 5, 10, 5, 5, 5, 20, 20, 20, 10, 5, 5, 20, 5, 5, 10, 5, 20, 5, 10, 5, 20, 5, 5, 5, 10, 5, 10, 5, 20, 10, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 10, 5, 5, 20, 20, 5, 5, 10, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 5, 10, 5, 20, 5, 5, 20, 20, 5, 5, 5, 10, 10, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 20, 10, 20, 20, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 20, 5, 5, 20, 5, 5, 10, 10, 5, 20, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 10, 20, 5, 5, 10, 20, 5, 10, 5, 20, 10, 5, 5, 5, 20, 5, 10, 20, 5, 5, 20, 20, 10, 5, 5, 5, 20, 5, 5, 10, 10, 20, 5, 20, 10, 5, 5, 5, 10, 10, 20, 20, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 20, 5, 5, 20, 5, 10, 5, 5, 10, 10, 5, 5, 5, 20, 5, 20, 10, 5, 5, 5, 5, 20, 10, 10, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 10, 5, 10, 10, 5, 5, 5, 10, 20, 10, 10, 5, 20, 20, 5, 5, 5, 20, 5, 10, 5, 20, 5, 5, 20, 5, 5, 20, 10, 10, 5, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 20, 10, 10, 5, 20, 5, 10, 5, 5, 20, 5, 20, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 10, 5, 5, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 20, 10, 20, 5, 5, 5, 20, 20, 5, 20, 5, 10, 5, 10, 5, 5, 10, 5, 5, 20, 5, 5, 20, 5, 20, 5, 10, 5, 5, 10, 10, 20, 10, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 10, 20, 5, 10, 5, 20, 10, 10, 5, 10, 5, 20, 5, 5, 5, 10, 20, 5, 5, 5, 20, 5, 20, 5, 10, 5, 5, 5, 5, 5, 20, 5, 10, 20, 20, 5, 5, 5, 20, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 20, 5, 20, 5, 5, 10, 20, 20, 10, 5, 20, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 20, 10, 5, 20, 10, 5, 10, 20, 5, 5, 5, 5, 20, 10, 5, 5, 20, 10, 5, 10, 20, 10, 20, 5, 20, 10, 20, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 10, 5, 10, 5, 20, 10, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 20, 5, 10, 5, 20, 5, 10, 5, 5, 5, 5, 10, 10, 5, 20, 5, 5, 20, 5, 5, 5, 5, 20, 20, 5, 5, 20, 5, 5, 5, 5, 5, 20, 20, 5, 10, 20, 5, 5, 5, 5, 5, 10, 10, 20, 10, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 20, 10, 5, 20, 5, 5, 20, 10, 5, 10, 5, 10, 5, 5, 5, 10, 20, 20, 5, 10, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 20, 5, 10, 20, 5, 5, 5, 10, 5, 10, 5, 20, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 10, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 10, 5, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 20, 10, 20, 5, 5, 20, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 20, 5, 5, 10, 20, 5, 5, 5, 10, 5, 20, 20, 5, 20, 5, 10, 20, 20, 5, 5, 20, 10, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 20, 20, 5, 20, 10, 10, 10, 20, 5, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 10, 20, 20, 10, 5, 10, 5, 20, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 5, 5, 5, 10, 20, 20, 5, 5, 20, 5, 5, 5, 10, 5, 10, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 10, 20, 20, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 10, 5, 10, 10, 5, 20, 5, 10, 10, 20, 10, 5, 10, 20, 5, 5, 20, 5, 10, 5, 5, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 5, 20, 5, 20, 5, 20, 10, 20, 5, 20, 5, 10, 10, 20, 5, 5, 10, 20, 5, 20, 20, 5, 20, 20, 10, 10, 10, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 20, 10, 5, 5, 5, 20, 5, 10, 20, 5, 20, 5, 5, 5, 10, 10, 5, 5, 5, 10, 20, 10, 10, 10, 5, 20, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 5, 10, 5, 20, 20, 5, 20, 5, 20, 10, 5, 5, 5, 10, 5, 10, 5, 20, 5, 5, 10, 5, 5, 20, 20, 20, 5, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5, 5, 5, 5, 20, 20, 20, 5, 20, 20, 10, 5, 5, 20, 5, 20, 20, 5, 5, 5, 5, 20, 10, 5, 20, 10, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 10, 10, 20, 10, 5, 5, 5, 5, 5, 20, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 5, 5, 20, 5, 10, 20, 5, 20, 5, 20, 10, 10, 5, 20, 5, 5, 5, 20, 10, 5, 20, 5, 10, 10, 5, 20, 5, 5, 10, 20, 5, 5, 5, 20, 10, 5, 20, 20, 10, 20, 5, 20, 5, 10, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 10, 20, 10, 10, 5, 5, 5, 5, 5, 10, 10, 20, 20, 20, 10, 10, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 20, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 10, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 20, 20, 5, 5, 20, 10, 20, 20, 20, 10, 20, 5, 20, 5, 10, 5, 5, 5, 10, 20, 20, 5, 5, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 10, 10, 5, 20, 5, 10, 20, 5, 5, 5, 20, 5, 10, 10, 10, 5, 10, 5, 20, 5, 5, 5, 5, 10, 5, 5, 10, 10, 5, 5, 5, 10, 20, 10, 20, 5, 20, 5, 5, 10, 10, 5, 10, 5, 5, 5, 5, 20, 10, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 20, 5, 5, 10, 10, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 20, 10, 5, 10, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20, 5, 10, 10, 5, 20, 5, 10, 5, 5, 20, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 5, 10, 20, 10, 5, 5, 10, 5, 5, 20, 20, 5, 10, 10, 10, 20, 5, 5, 5, 10, 5, 5, 5, 5, 10, 10, 20, 20, 5, 10, 10, 20, 5, 20, 10, 20, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 10, 5, 5, 5, 5, 10, 20, 5, 5, 20, 5, 5, 20, 5, 20, 20, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 20, 5, 5, 10, 20, 10, 10, 5, 20, 10, 5, 20, 20, 5, 5, 5, 5, 5, 5, 10, 20, 5, 20, 5, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 10, 10, 5, 10, 20, 5, 5, 10, 20, 20, 20, 20, 5, 20, 10, 10, 5, 10, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 10, 5, 5, 10, 20, 5, 20, 5, 5, 20, 20, 10, 20, 5, 10, 10, 5, 5, 10, 20, 5, 5, 5, 20, 5, 20, 5, 20, 10, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 20, 20, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 5, 10, 10, 20, 5, 20, 20, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5, 20, 5, 5, 5, 10, 20, 5, 5, 20, 5, 20, 5, 5, 10, 5, 20, 20, 5, 5, 20, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 20, 10, 5, 5, 5, 20, 10, 5, 5, 10, 5, 5, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 5, 10, 10, 5, 20, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 10, 5, 10, 10, 20, 5, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 20, 10, 20, 20, 5, 10, 20, 5, 5, 20, 5, 5, 20, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 10, 10, 20, 5, 10, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 20, 5, 20, 10, 10, 5, 5, 10, 5, 5, 10, 5, 20, 5, 10, 20, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 10, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 20, 20, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 10, 5, 5, 20, 5, 10, 10, 5, 5, 10, 20, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 10, 20, 5, 5, 20, 5, 5, 20, 20, 5, 20, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 20, 20, 10, 10, 5, 10, 5, 5, 20, 5, 10, 5, 20, 10, 20, 10, 5, 5, 10, 10, 5, 5, 5, 20, 20, 5, 5, 5, 5, 20, 5, 20, 5, 5, 20, 10, 5, 20, 5, 5, 5, 5, 20, 5, 10, 20, 10, 10, 5, 10, 5, 10, 5, 10, 5, 10, 10, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 20, 20, 5, 5, 5, 10, 10, 10, 5, 5, 10, 5, 10, 10, 5, 5, 20, 5, 10, 20, 10, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 10, 5, 5, 10, 10, 10, 5, 10, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 20, 5, 5, 20, 5, 5, 20, 5, 5, 10, 10, 5, 10, 5, 5, 5, 20, 5, 10, 5, 10, 5, 5, 10, 5, 20, 5, 10, 5, 10, 10, 20, 10, 5, 20, 10, 5, 5, 5, 10, 5, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 10, 5, 5, 10, 20, 5, 5, 20, 5, 5, 20, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 20, 5, 5, 20, 20, 5, 5, 20, 20, 20, 5, 10, 5, 5, 20, 5, 10, 5, 5, 20, 10, 5, 20, 20, 5, 10, 5, 20, 20, 5, 5, 5, 10, 5, 10, 5, 20, 20, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 10, 20, 10, 5, 20, 5, 5, 20, 5, 5, 20, 20, 10, 5, 20, 20, 5, 5, 10, 5, 20, 5, 5, 20, 10, 5, 5, 5, 20, 5, 5, 5, 20, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 5, 5, 20, 20, 10, 5, 5, 20, 10, 10, 5, 20, 5, 5, 20, 10, 20, 5, 20, 5, 5, 20, 5, 20, 10, 20, 20, 20, 5, 5, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 10, 5, 20, 10, 5, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 10, 5, 5, 10, 20, 5, 5, 20, 5, 5, 5, 10, 20, 20, 5, 5, 5, 20, 5, 5, 20, 5, 20, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 20, 10, 10, 20, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 20, 5, 10, 10, 5, 10, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 10, 5, 20, 10, 5, 5, 20, 10, 10, 10, 20, 5, 10, 5, 5, 20, 5, 20, 5, 20, 5, 20, 10, 5, 5, 5, 5, 10, 5, 10, 10, 5, 5, 5, 20, 5, 5, 20, 5, 5, 5, 20, 10, 5, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 20, 20, 5, 20, 5, 10, 5, 20, 20, 10, 10, 20, 10, 20, 10, 5, 10, 10, 5, 5, 10, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 10, 10, 20, 5, 5, 5, 5, 5, 20, 5, 10, 20, 5, 5, 20, 5, 10, 5, 5, 5, 10, 20, 5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 20, 20, 10, 5, 20, 10, 5, 10, 5, 5, 5, 5, 10, 5, 10, 5, 20, 5, 20, 5, 10, 5, 5, 5, 5, 10, 20, 5, 10, 5, 5, 5, 10, 5, 20, 5, 5, 20, 5, 5, 5, 20, 5, 20, 5, 5, 5, 10, 5, 10, 10, 10, 10, 20, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 20, 5, 20, 5, 10, 5, 10, 5, 20, 20, 20, 5, 5, 20, 5, 5, 20, 20, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 20, 10, 5, 5, 20, 5, 5, 20, 5, 20, 5, 20, 5, 20, 5, 10, 5, 20, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 10, 5, 5, 5, 10, 10, 5, 20, 10, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 10, 20, 10, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 20, 5, 20, 5, 20, 5, 5, 10, 10, 5, 5, 10, 20, 5, 5, 20, 20, 5, 5, 5, 20, 10, 20, 5, 10, 5, 20, 20, 5, 5, 5, 10, 10, 5, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 20, 20, 10, 20, 10, 5, 5, 20, 5, 5, 5, 20, 10, 5, 10, 10, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 10, 5, 20, 5, 10, 20, 5, 5, 5, 10, 5, 5, 20, 5, 10, 5, 10, 5, 5, 5, 20, 5, 20, 5, 20, 5, 10, 5, 20, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 10, 5, 5, 10, 20, 10, 5, 10, 5, 5, 5, 20, 5, 10, 5, 10, 5, 5, 10, 20, 5, 10, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 10, 20, 10, 10, 20, 5, 5, 5, 5, 20, 5, 5, 5, 20, 20, 20, 5, 20, 5, 20, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 20, 10, 5, 5, 10, 20, 5, 10, 10, 5, 5, 5, 5, 20, 5, 20, 20, 5, 5, 5, 10, 5, 10, 20, 10, 5, 5, 20, 5, 20, 5, 20, 5, 5, 5, 20, 20, 5, 10, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 5, 10, 5, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 20, 10, 5, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 20, 5, 20, 5, 10, 20, 5, 5, 10, 5, 10, 5, 5, 5, 10, 20, 20, 5, 5, 10, 10, 10, 10, 5, 5, 10, 5, 5, 10, 20, 20, 10, 20, 10, 20, 10, 20, 5, 20, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 20, 5, 10, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 20, 5, 20, 10, 5, 20, 5, 5, 20, 5, 20, 5, 10, 10, 10, 5, 5, 5, 10, 10, 5, 10, 10, 10, 5, 20, 20, 5, 5, 5, 20, 10, 20, 20, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 5, 10, 10, 20, 5, 20, 5, 20, 20, 20, 5, 20, 10, 5, 5, 5, 10, 20, 20, 5, 5, 5, 5, 5, 20, 10, 20, 5, 5, 10, 5, 5, 10, 5, 10, 5, 10, 10, 20, 5, 5, 20, 5, 10, 20, 10, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 10, 5, 5, 20, 5, 20, 5, 10, 5, 20, 10, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 10, 5, 20, 10, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 10, 5, 5, 10, 5, 5, 5, 10, 20, 10, 20, 20, 20, 5, 5, 5, 5, 10, 5, 5, 5, 20, 20, 20, 5, 20, 10, 5, 10, 10, 5, 5, 5, 10, 20, 5, 10, 5, 5, 5, 10, 20, 5, 5, 20, 20, 10, 5, 5, 10, 10, 5, 20, 5, 5, 20, 5, 5, 20, 5, 20, 20, 5, 20, 20, 10, 5, 20, 5, 5, 5, 5, 20, 20, 5, 5, 5, 20, 20, 5, 10, 20, 10, 5, 5, 5, 5, 5, 20, 20, 20, 5, 5, 5, 5, 5, 5, 10, 5, 10, 20, 20, 5, 5, 20, 5, 20, 20, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 10, 5, 10, 20, 5, 20, 5, 5, 5, 5, 20, 5, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 20, 20, 10, 5, 10, 5, 5, 20, 10, 10, 5, 5, 5, 20, 5, 20, 10, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 20, 5, 5, 10, 5, 5, 20, 5, 5, 10, 5, 20, 10, 10, 10, 5, 5, 5, 10, 10, 20, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 10, 5, 5, 10, 20, 5, 5, 20, 5, 10, 10, 5, 10, 20, 5, 5, 5, 5, 10, 10, 5, 5, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 20, 20, 5, 5, 10, 10, 5, 5, 20, 20, 10, 5, 5, 20, 10, 20, 5, 5, 10, 20, 5, 10, 5, 10, 20, 5, 20, 10, 20, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 20, 10, 10, 5, 20, 20, 10, 10, 20, 20, 10, 5, 5, 5, 10, 5, 10, 5, 5, 20, 10, 5, 5, 5, 5, 20, 5, 10, 5, 5, 10, 20, 5, 20, 10, 5, 5, 5, 5, 20, 5, 10, 10, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20, 5, 5, 5, 20, 5, 20, 5, 5, 5, 5, 10, 20, 20, 10, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 20, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 20, 20, 10, 20, 10, 5, 10, 5, 10, 20, 10, 5, 5, 5, 20, 10, 5, 5, 5, 5, 5, 5, 10, 10, 5, 20, 10, 10, 5, 5, 5, 5, 5, 10, 5, 5, 10, 10, 20, 5, 5, 20, 5, 5, 5, 10, 10, 20, 10, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 5, 10, 5, 20, 20, 5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 10, 10, 20, 5, 5, 5, 20, 10, 10, 5, 5, 20, 10, 5, 5, 20, 10, 10, 10, 5, 10, 5, 5, 5, 20, 5, 10, 20, 5, 20, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 5, 5, 10, 5, 10, 5, 5, 5, 20, 10, 10, 5, 5, 5, 20, 20, 20, 10, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 10, 5, 10, 5, 5, 5, 10, 20, 20, 5, 10, 5, 10, 5, 5, 5, 10, 5, 5, 5, 10, 5, 5, 20, 10, 20, 5, 20, 5, 5, 10, 10, 20, 10, 20, 5, 20, 5, 5, 10, 5, 5, 10, 5, 20, 5, 5, 5, 10, 5, 5, 5, 10, 10, 20, 5, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 20, 5, 5, 10, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 10, 10, 20, 10, 5, 5, 5, 10, 20, 5, 5, 5, 5, 5, 20, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 10, 5, 20, 5, 10, 5, 20, 20, 5, 20, 10, 5, 5, 5, 20, 5, 20, 5, 5, 10, 5, 5, 20, 20, 5, 5, 5, 5, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 10, 20, 5, 5, 20, 5, 5, 5, 20, 10, 10, 5, 5, 10, 5, 5, 20, 5, 10, 5, 5, 10, 20, 10, 10, 20, 20, 20, 10, 20, 10, 10, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 20, 5, 10, 20, 10, 20, 10, 5, 5, 5, 5, 5, 20, 5, 10, 10, 5, 5, 5, 5, 10, 10, 5, 5, 20, 10, 10, 5, 10, 10, 5, 5, 5, 5, 20, 10, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 20, 5, 20, 5, 10, 10, 10, 5, 20, 5, 5, 5, 5, 10, 10, 5, 5, 20, 20, 5, 5, 10, 10, 5, 5, 20, 5, 20, 20, 5, 5, 5, 5, 10, 5, 20, 5, 5, 20, 10, 5, 5, 5, 20, 20, 20, 5, 5, 5, 5, 5, 20, 5, 5, 20, 20, 20, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 10, 5, 5, 20, 5, 5, 10, 20, 5, 5, 5, 5, 5, 10, 20, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 5, 5, 10, 5, 5, 5, 5, 20, 5, 5, 10, 10, 20, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 20, 10, 20, 5, 20, 5, 5, 5, 5, 20, 10, 5, 10, 20, 5, 10, 5, 20, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 20, 5, 5, 10, 5, 10, 10, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 5, 20, 5, 10, 20, 5, 20, 20, 5, 10, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 20, 5, 10, 5, 5, 5, 10, 20, 5, 10, 5, 5, 5, 5, 5, 20, 10, 10, 10, 10, 5, 20, 5, 5, 10, 5, 5, 20, 10, 5, 10, 5, 5, 5, 5, 20, 5, 5, 10, 10, 5, 5, 10, 5, 5, 10, 10, 20, 5, 5, 5, 5, 20, 5, 10, 10, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 20, 10, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 10, 20, 20, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20, 20, 5, 5, 5, 10, 5, 5, 10, 20, 5, 20, 5, 5, 20, 5, 10, 5, 5, 10, 20, 5, 10, 20, 10, 5, 10, 5, 20, 10, 5, 20, 10, 5, 20, 20, 5, 5, 20, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 10, 5, 5, 20, 20, 5, 5, 20, 20, 10, 5, 5, 10, 20, 20, 5, 5, 10, 10, 10, 5, 5, 5, 5, 20, 5, 5, 20, 5, 10, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 10, 5, 5, 5, 5, 5, 10, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 20, 10, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 20, 20, 5, 20, 5, 5, 5, 10, 5, 20, 20, 20, 5, 20, 10, 10, 20, 5, 20, 5, 5, 5, 10, 20, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 20, 5, 10, 5, 10, 5, 20, 20, 5, 10, 20, 5, 20, 5, 5, 20, 5, 20, 5, 10, 5, 10, 5, 5, 5, 20, 20, 5, 10, 5, 5, 10, 10, 20, 10, 5, 20, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 20, 10, 5, 20, 10, 20, 20, 20, 5, 10, 20, 10, 20, 20, 20, 10, 5, 5, 5, 5, 10, 5, 10, 5, 10, 10, 10, 20, 20, 5, 5, 5, 5, 5, 5, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 20, 5, 5, 20, 20, 10, 5, 5, 10, 10, 5, 20, 20, 5, 5, 10, 5, 20, 10, 20, 20, 10, 10, 20, 20, 20, 5, 5, 10, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 20, 10, 5, 5, 5, 10, 5, 20, 5, 10, 10, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5, 5, 10, 5, 20, 10, 20, 5, 5, 10, 5, 5, 20, 10, 5, 10, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 20, 5, 10, 10, 20, 10, 5, 20, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 5, 10, 10, 20, 5, 20, 10, 5, 5, 10, 20, 20, 20, 10, 5, 5, 5, 5, 5, 10, 20, 5, 5, 5, 10, 20, 5, 20, 10, 10, 20, 5, 5, 10, 20, 10, 20, 5, 10, 10, 10, 10, 5, 5, 10, 20, 10, 10, 5, 5, 5, 10, 20, 5, 5, 10, 5, 5, 10, 20, 5, 5, 5, 5, 10, 10, 5, 20, 5, 20, 5, 20, 5, 20, 5, 5, 20, 10, 5, 20, 5, 5, 5, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 10, 10, 5, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 10, 5, 5, 10, 5, 20, 20, 5, 5, 5, 20, 10, 5, 5, 5, 5, 20, 10, 5, 5, 10, 10, 20, 10, 10, 10, 20, 10, 5, 5, 5, 5, 20, 20, 5, 5, 10, 20, 5, 5, 20, 5, 20, 10, 20, 5, 5, 5, 5, 10, 10, 5, 5, 5, 20, 5, 20, 5, 20, 5, 10, 5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 20, 5, 5, 20, 10, 5, 10, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 10, 10, 5, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 10, 10, 20, 5, 5, 5, 5, 5, 10, 5, 5, 5, 20, 10, 5, 10, 5, 10, 10, 20, 20, 10, 5, 5, 20, 5, 10, 5, 5, 5, 5, 5, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 5, 5, 20, 5, 10, 5, 5, 10, 20, 5, 20, 20, 5, 10, 5, 20, 5, 5, 5, 5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 5, 5, 5, 10, 20, 20, 5, 20, 20, 5, 5, 5, 20, 5, 20, 5, 20, 20, 5, 10, 5, 10, 5, 10, 5, 5, 10, 5, 5, 10, 5, 10, 20, 20, 10, 5, 5, 20, 10, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 20, 5, 5, 5, 5, 20, 10, 5, 20, 5, 10, 5, 5, 5, 5], True),
        ]
for bills, expected in data:
    real = s.lemonadeChange(bills)
    if 10 < len(bills):
        print('{}..., expected {}, real {}, result {}'.format(bills[:10], expected, real, expected == real))
    else:
        print('{}, expected {}, real {}, result {}'.format(bills, expected, real, expected == real))
