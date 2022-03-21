
# recursive solutions not possible even with memo, because of stack size limit
# had to lookup hints, essentially a proof exists that we will find optimals ops if:
#  - divide if last bit is 0
#  - subtract 1 if last two bits are 01
#  - add 1 if last two bits are 11

def solve(n):
    ops = 0
    while True:
    	if n <= 1:
    		return ops
    	if n == 2:
    		return 1 + ops
    	if n == 3:
    		return 2 + ops
    	if n%4 == 0:
    		ops += 2 
    		n = n//4
    	elif n%4 == 2:
    		ops += 1
    		n = n//2
    	elif n%4 == 1:
    		ops += 1
    		n -= 1
    	elif n%4 == 3:
    		ops += 1 
    		n += 1

def solution(n):
	return solve(int(n))


# print(solution("1"*309))
print(solution("15"))
print(solution("4"))
print(solution("3"))