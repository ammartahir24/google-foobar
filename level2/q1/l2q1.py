


def move(i):
	# returns list of valid knight moves from i
	x = int(i/8)
	y = i%8
	pos = []
	moves = [(-2,-1), (-2,1), (-1,-2), (1,-2), (-1,2), (1,2), (2,-1), (2,1)]
	for m in moves:
		box_x, box_y = x + m[0], y + m[1]
		box = box_x*8 + box_y
		if box_x >= 8 or box_x < 0 or box_y >= 8 or box_y < 0 or box < 0 or box >63:
			continue
		pos += [box]
	return pos


# Using a bottom-up DP approach, recursion + memo can also be used, arguing about bottom-ups time complexity is easier
# start growing from dest to src, keeping track of distance of every box from dest
def solution(src, dest):
	#Your code here
	to_expand = [dest]		# list of nodes to expand
	expanded = {}
	expanded[dest] = 0
	if src == dest:
		return 0
	for d in to_expand:
		all_moves = move(d)
		for m in all_moves:
			if m not in expanded:
				to_expand.append(m)
				expanded[m] = 1 + expanded[d]
				if m == src:
					return expanded[src]
	

print(solution(10, 54))
print(solution(27, 44))
print(solution(0, 0))