#   https://leetcode.com/problems/rotting-oranges

#   https://leetcode.com/problems/rotting-oranges/solution


class Solution:
    #   runtime; 44ms, 100.00%
    #   memory; 10.8MB, 100.00%
    def orangesRotting(self, grid):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return -1

        if 1 == len(grid) and 1 == len(grid[0]):
            if 1 == grid[0][0]:
                return -1
            return 0

        row, col = len(grid), len(grid[0])
        times, starts = [[row * col] * col for _ in range(row)], []
        for r in range(row):
            for c in range(col):
                if 0 == grid[r][c]:
                    times[r][c] = -1
                if 2 == grid[r][c]:
                    starts.append((r, c))
                    times[r][c] = 0

        def getMinRotting(r, c, val):
            times[r][c] = min(times[r][c], val)
            #print('\tpoint[{}][{}] = {}'.format(r, c, times[r][c]))
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < row and 0 <= nc < col and 1 == grid[nr][nc] and times[r][c] < times[nr][nc]:
                    times[nr][nc] = min(times[nr][nc], val + 1)
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < row and 0 <= nc < col and 1 == grid[nr][nc] and times[r][c] < times[nr][nc]:
                    getMinRotting(nr, nc, val + 1)

        while starts:
            r, c = starts.pop(0)
            #print('start from {}, {}'.format(r, c))
            #print('\t', grid)
            #print('\t', times)
            getMinRotting(r, c, 0)
            #print('\t', grid)
            #print('\t', times)
        res = 0
        for r in range(row):
            for c in range(col):
                if 0 == grid[r][c]:
                    continue
                if row * col == times[r][c]:
                    return -1
                res = max(res, times[r][c])
        return res


s = Solution()
data = [([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0),
        ([[0]], 0),
        ([[1]], -1),
        ([[1], [2], [2]], 1),
        ([[0, 0, 1, 2], [2, 0, 1, 1]], 2),
        ([[0, 1, 1, 2], [0, 1, 1, 0], [1, 1, 2, 0]], 2),
        ]
for grid, expected in data:
    real = s.orangesRotting(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
'''
2 1 1   0 0 0
1 1 0   0 0 -
0 1 1   - 0 0

2 1 1
0 1 1
1 0 1

0 2

0 0 1 2
2 0 1 1

0 1 1 2
0 1 1 0
1 1 2 0
'''
