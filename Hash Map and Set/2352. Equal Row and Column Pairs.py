# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
# such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order 
# (i.e., an equal array).

# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

#we want to compare 2 things: rows and columns
#we can each row and each col as hash
#check if hash and rows are equal in values and order
#if so return the index


from collections import defaultdict
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        pairs = 0 
        #stores counter for rows into key of the defaultdict rows
        for row in grid:
            rows[tuple(row)] += 1 
        
        #tuple for the columns in grid
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            #if the col is found in the row dict 
            #store that pair into pairs var
            if column in rows: 
                pairs += rows[column]
        return pairs

c = Solution()
test1 = c.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
print(test1)
