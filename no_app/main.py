# Copyright (c) 2021 Belmont Technology Inc. All rights reserved.

from math import sqrt
import random

#######################################################
def check_if_prime(n):

	prime_flag = 0

	if(n > 1):
		for i in range(2, int(sqrt(n)) + 1):
			if (n % i == 0):
				prime_flag = 1
				break
		if (prime_flag == 0):
			return True
		else:
			return False
	else:
		return False

#######################################################
if __name__ == '__main__':

	n = random.randint(0, 10000)
	status = check_if_prime(n)
	if status:
		print(str(n) + " is a prime number")
	else:
		print(str(n) + " is NOT a prime number")
