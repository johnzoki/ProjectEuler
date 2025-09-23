'''
Author: John Zoki
Multiples of 3 or 5
Problem 1:
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
Answer: 233168
Completed on Sun, 1 Aug 2021, 22:22
'''

import time

tic=time.perf_counter()

numbers = []
for number in range(3, 1000):
	if number % 3 == 0 or number % 5 == 0:
		numbers.append(number)
print(sum(numbers))

toc=time.perf_counter()
print(f"Solved the task in {toc-tic} sec")