'''
Author: John Zoki
Largest palindrome product
Problem 4:
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 906609
Completed on on Mon, 2 Aug 2021, 13:10
'''

import time

tic=time.perf_counter()

palindromicNumber = 700000
a = range(100, 1000)
b = 1000

for n in a[::-1]:
	b = 1000
	while b > 100:
		b += -1
		if len(str(b * n)) > 5 and b * n > palindromicNumber:
			if str(b * n)[0] == str(b * n)[-1] and str(b * n)[1] == str(b * n)[-2] and str(b * n)[2] == str(b * n)[-3]:
				palindromicNumber = b * n
				print(palindromicNumber)

toc=time.perf_counter()
print(f"Solved the task in {toc-tic} sec")