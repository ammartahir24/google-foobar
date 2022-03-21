import numpy as np


def nextp(i):
    # returns prime number after i
    # complexity = O(c x sqrt(n)), where c is distance between two prime numbers
	while True:
		i+=1
		isprime = True
		for k in range(2,int(np.sqrt(i)+1)):
			if i % k == 0:
				isprime = False
		if isprime:
			return i

def solution(i):
    # Your code here
    prime = 2
    prime_string_len = 1
    
    # find primes until string length is reached O(n x sqrt(n))
    while i>=prime_string_len:
        prime = nextp(prime)
        prime_string_len += len(str(prime))
        
    length = prime_string_len - i
    p_string = str(prime)
    prime_string = p_string[len(p_string) - length:]
    length = len(prime_string)

    # find next 5 digits of string
    while length < 5:
    	prime = nextp(prime)
    	prime_string += str(prime)
    	length = len(prime_string)


    return int(prime_string[0:5])



print(solution(0))
print(solution(3))
print(solution(1))
print(solution(2))
print(solution(6))
print(solution(10000))