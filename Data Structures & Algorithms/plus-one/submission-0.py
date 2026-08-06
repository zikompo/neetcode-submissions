class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for num in digits:
            s += str(num)

        number = int(s)
        number += 1
        ret = []
        for num in str(number):
            ret.append(int(num))
        return ret
