class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                scores.pop()
            elif operations[i] == 'D':
                scores.append(scores[-1]*2)
            elif operations[i] == '+':
                scores.append(scores[-1]+scores[-2])
            else:
                scores.append(int(operations[i]))
        
        if len(scores)==0:
            return 0

        sum=0
        for score in scores:
            sum+=score
        return sum