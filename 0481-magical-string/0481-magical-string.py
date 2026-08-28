class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        s = [1, 2, 2]
        count = 1
        i = 2
        num = 1
        while len(s) < n:
            times = s[i]
            for _ in range(times):
                if len(s) >= n:
                    break
                s.append(num)
                if num == 1:
                    count += 1
            num = 3 - num
            i += 1
        return count