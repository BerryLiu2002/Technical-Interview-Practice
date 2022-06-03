"""
Question Name: 542. 01 Matrix
Difficulty: Medium
Category: Graph (DFS)
Link: https://leetcode.com/problems/01-matrix/
"""

"""
Solution 1: Completed one interation of the matrix. Calls bfs on each non-0 which finds the closest 0.
Runtime: O(n^4) Too Slow
"""
# from collections import deque
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         num_rows, num_cols = len(mat), len(mat[0])
#         # res = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
#         def bfs(r,c):
#             dirs = [(1,0), (-1,0), (0,1), (0,-1)]
#             seen = set()
#             level = 0
#             stack = deque()
#             stack.append((r,c))
#             while stack:
#                 ll = len(stack)
#                 for i in range(ll):
#                     r,c = stack.popleft()
#                     seen.add((r,c))
#                     if mat[r][c] == 0:
#                         return level
#                     for x,y in dirs:
#                         nr, nc = r+x, c+y
#                         if nr < num_rows and nc < num_cols and nr >= 0 and nc >= 0 and (nr,nc) not in seen:
#                             stack.append((nr,nc))
#                 level += 1
                      
#         for r in range(num_rows):
#             for c in range(num_cols):
#                 if mat[r][c]:
#                     dist = bfs(r,c)
#                     mat[r][c] = dist
#         return mat

"""
Solution 2: Completed one interation of the matrix, records all 0. 
Simutaneous call bfs on each 0 and mark each non-0 according to the level of the bfs call as it reaches the point..
Runtime: O(n^2+n^2) = O(n^2)
"""
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        num_rows, num_cols = len(mat), len(mat[0])
        ripple = deque()
        for r in range(num_rows):
            for c in range(num_cols):
                if mat[r][c] == 0:
                    ripple.append((r,c))
                    seen.add((r,c))
        level = 0
        while ripple:
            for _ in range(len(ripple)):
                r,c = ripple.popleft()
                mat[r][c] = level
                for x,y in dirs:
                    nr, nc = r+x, c+y
                    if nr < num_rows and nc < num_cols and nr >= 0 and nc >= 0 and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        ripple.append((nr,nc))
            level += 1
        return mat

