# You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# Complexity: O(log(n))


class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1:
            return 1
        elif x ==0:
            return 0
        else :
            l=0
            r= x
            res =0
            while l<=r:
                middle = (l+r)//2
                print(middle)
                if (middle*middle) ==x:
                    return middle
                elif (middle*middle)<x:
                    l = middle+1
                    res = middle
                else:
                    r = middle-1
            return res
