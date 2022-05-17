from math import sqrt
import random
import streamlit as st

#######################################################
def __check_status__(n):

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

	st.title("Check if prime number")
	n = st.text_input('Insert an integer', value="0")

	status = __check_status__(int(n))
	if status:
		st.text(str(n) + " is a prime number")
	else:
		st.text(str(n) + " is NOT a prime number")
