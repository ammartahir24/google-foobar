from fractions import Fraction

def printmtx(m):
	print("")
	for row in m:
		print(row)

def construct_QR(m):
	transient, terminal = [], []
	for i in range(len(m)):
		row = m[i]
		if all([x==0 for x in row]):
		# if sum(m[i]) == m[i][i]:
			terminal.append(i)
		else:
			transient.append(i)
	# print(terminal, transient)
	
	Q, R = [], []
	for j in range(len(m)):
		row = m[j]
		if j in transient:
			rowQ, rowR = [], []
			totalP = sum(row)
			for i in range(len(row)):
				if i in transient:
					rowQ.append(Fraction(row[i], totalP))
				elif i in terminal:
					rowR.append(Fraction(row[i], totalP))
			Q.append(rowQ)
			R.append(rowR)
	# printmtx(Q)
	# printmtx(R)
	return Q, R, len(transient), len(terminal)

def identity(x):
	return [[0 if i!=j else 1 for j in range(x)] for i in range(x)]

def subtract(m1, m2):
	diff = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
	return diff

def copy(m):
	return [[m[i][j] for j in range(len(m[i]))] for i in range(len(m))]


def flip(m):
	# print(m)
	m2 = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
	for i in range(len(m)):
		for j in range(len(m[i])):
			m2[j][i] = m[i][j]
	return m2


def multiply(m1, m2):
	if m1 == [] or m2 == []:
		return []
	ret = []
	m2_ = flip(m2)
	for row in m1:
		r = []
		for col in m2_:
			r.append(sum([row[i]*col[i] for i in range(len(row))]))
		ret.append(r)
	return ret



def inverse(m):
	# using row operations
	# printmtx(m)
	I_AM = identity(len(m))
	M_AM = copy(m)

	for i in range(len(m)):
		scale = M_AM[i][i]
		if scale == 0:
			# find new pivot
			for k in range(i+1, len(m)):
				if M_AM[k][i] != 0:
					# swap
					temp = M_AM[i]
					M_AM[i] = M_AM[k]
					M_AM[k] = temp
					temp = I_AM[i]
					I_AM[i] = I_AM[k]
					I_AM[k] = temp
					scale = M_AM[i][i]
					break

		for j in range(len(m)):
			M_AM[i][j]/=scale
			I_AM[i][j]/=scale

		for i2 in range(len(m)):
			if i2!=i:
				scale = M_AM[i2][i]
				for j in range(len(m)):
					M_AM[i2][j] -= scale*M_AM[i][j]
					I_AM[i2][j] -= scale*I_AM[i][j]

	# printmtx(M_AM)
	# printmtx(I_AM)
	# printmtx(multiply(m, I_AM))
	return I_AM

def gcd(a ,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

# def gcd(x,y):
# 	div = min(x,y)
# 	while x%div !=0 and y%div != 0:
# 		div -= 1
# 	return div

def lcm_gcd(x,y):
	return (x*y)/gcd(x,y)

def lcm(xs):
	lcm_ = 1
	for x in xs:
		lcm_ = lcm_gcd(lcm_, x)
	return lcm_


# we need to find absorbing probabilities as defined here: https://en.wikipedia.org/wiki/Absorbing_Markov_chain
def solution(m):
	# printmtx(m)
	Q, R, num_transient, num_terminal = construct_QR(m)

	I_transient = identity(num_transient)
	# printmtx(I_transient)
	N = inverse(subtract(I_transient, Q))
	# printmtx(N)
	# print(Q)
	# print(N)
	# print(R)
	B = multiply(N, R)

	if sum(m[0])==m[0][0]:
		return [1] + [0 for x in range(num_terminal-1)] + [1]

	if B == []:
		return [1] + [0 for x in range(num_terminal-1)] + [1]

	ans = B[0]
	lcm_ = lcm([x.denominator for x in ans])
	ret = [(x*int(lcm_)).numerator for x in ans] + [int(lcm_)]
	return ret

# def numerate(m):
# 	return [[Fraction(x) for x in r] for r in m]
# print(inverse([[0,1],[1,1]]))
# print(inverse(numerate([[0,11,2],[4,0,3], [1,2,3]])))
# print(inverse(numerate([[0,1,0],[1,0,0], [0,0,-1]])))



# print(solution([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
# print(solution([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# print(solution([[0, 1], [0, 1]]))
print(solution([[0]]))
# print(solution([[1, 0], [0, 1]]))
# print(solution([[0, 2, 7], [0, 0, 0], [0, 0, 0]]))
# print(solution([[1, 1, 1], [1, 1, 1], [0, 0, 1]]))
# print(solution([[1, 1, 1], [1, 1, 1], [0, 0, 0]]))
# print(solution([[1, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))