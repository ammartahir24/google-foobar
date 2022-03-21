# import math

def printarr(arr):
	for x in arr:
		print(x)

# starting at 0,0 and with w=1, recursively find optimal way to l-1,h-1
# what is its time complexity?
def solve(map,i,j,w,memo):
	if i==len(map)-1 and j==len(map[0])-1:
		return 1
	if (i,j,w) in memo:
		return memo[(i,j,w)]
	results = []
	if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
		return 1000
	if w == 0 and map[i][j] == 1:
		return 1000
	if map[i][j] == 2:
		return 1000
	if w == 1 and map[i][j] == 1:
		w = 0
	val = map[i][j]
	# mark i,j as visited, so its not processed again in recursive calls
	map[i][j] = 2
	# 4 places we can go from i,j
	results.append(solve(map, i-1, j, w,memo))
	results.append(solve(map, i+1, j, w,memo))
	results.append(solve(map, i, j-1, w,memo))
	results.append(solve(map, i, j+1, w,memo))
	map[i][j] = val
	memo[(i,j,w)] = 1+min(results)
	return memo[(i,j,w)]


def solution(map):
    # Your code here
    memo = {}
    printarr(map)
    # map[0][0] = 2
    ans = solve(map,0,0,1,memo)
    return ans


print(solution([[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 1, 1], [0, 0, 0]]))
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))