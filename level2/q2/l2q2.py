def dist(pegs):
	dis = []
	for i in range(1, len(pegs)):
		dis.append(pegs[i]-pegs[i-1])
	return dis


# we need to solve following two equations:
# rn = dn - dn-1 + dn-2 - ... +d2 - d1 + r1
# rn = r1/2
# We first calculate di, with dist(), then calculate the sum of dis with alternate signs
def solution(pegs):
    # Your code here
    print(pegs)
    # distances = dist1(pegs)[::-1]
    distances = dist(pegs)[::-1]
    C = 0
    # print(distances2[::-1])
    for i in range(len(distances)):
    	if i % 2 == 0:
    		C += (distances[i])
    	else:
    		C -= (distances[i])
    # print(C)
    if len(distances) % 2 == 0:
    	if C > 0:
    		return [-1, -1]
    	else:
    		r = [-2*C, 1]
    else:
	    if C < 0:
	    	return [-1, -1]

	    C = 2*C
	    if C%3 == 0:
	    	r = [int(C/3), 1]
	    else:
	    	r = [C, 3]
    # print(r)
    rad = r[0]/r[1]
    # print(distances, rad)
    for d in distances[::-1]:
    	rad = d - rad
    	print(rad, d)
    	if rad < 1:
    		return [-1,-1]
    return r


print(solution([27, 30]))
print(solution([4, 30, 50]))
print(solution([4, 17, 50]))
print(solution([4, 8, 14, 22]))
print(solution([3, 6, 9, 12]))
print(solution([4, 10, 21, 30, 34]))
print(solution([4, 10, 21, 30, 33]))
print(solution([4, 10, 21, 30, 32]))
print(solution([4, 10, 21, 30, 31]))