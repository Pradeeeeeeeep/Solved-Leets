from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort()

        starts = [x[0] for x in arr]
        next_idx = [0] * n

        for i in range(n):
            right = arr[i][1]
            next_idx[i] = bisect_right(starts, right)

        prev = [(0, ()) for _ in range(n + 1)]

        for k in range(1, 5):
            cur = [(0, ()) for _ in range(n + 1)]

            for i in range(n - 1, -1, -1):
                skip_score, skip_indices = cur[i + 1]

                nxt = next_idx[i]
                take_score = arr[i][2] + prev[nxt][0]

                take_indices = tuple(
                    sorted((arr[i][3],) + prev[nxt][1])
                )

                if take_score > skip_score:
                    cur[i] = (take_score, take_indices)
                elif take_score < skip_score:
                    cur[i] = (skip_score, skip_indices)
                else:
                    if take_indices < skip_indices:
                        cur[i] = (take_score, take_indices)
                    else:
                        cur[i] = (skip_score, skip_indices)

            prev = cur

        return list(prev[0][1])