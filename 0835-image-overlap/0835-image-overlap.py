class Solution:
    def largestOverlap(self, img1, img2):
        shape1 = []
        shape2 = []
        rows, cols = len(img1), len(img1[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if img1[i][j] == 1:
                    shape1.append((i, j))


        for i in range(rows):
            for j in range(cols):
                if img2[i][j] == 1:
                    shape2.append((i, j))


        dic = defaultdict(int)

        for x1, y1 in shape1:
            for x2, y2 in shape2:
                dic[(x2 - x1, y2 - y1)] += 1

        return max(dic.values()) if dic.values() else 0