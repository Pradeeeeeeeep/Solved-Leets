class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(n):
            idx=i+1
            if idx%3==0 and idx%5==0:
                arr.append("FizzBuzz")
            elif idx%3==0:
                arr.append("Fizz")
            elif idx%5==0:
                arr.append("Buzz")
            else:
                arr.append(str(idx))
        return arr