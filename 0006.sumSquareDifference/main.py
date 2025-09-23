'''
Author: John Zoki
Sum square difference
Problem 6:
	The sum of the squares of the first ten natural numbers is,
	1 ** 2 + 2 ** 2 + ... 10 ** 2 = 385
	The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
	3025 - 385 = 2640.
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
Answer: 25164150
Completed on Mon, 2 Aug 2021, 17:42
'''

import time

tic=time.perf_counter()

numbers = range(1, 101)
firstP = 0
secondP = 0

for n in numbers:
	firstP += n ** 2
	secondP += n
secondP = secondP ** 2

print(secondP - firstP)

toc=time.perf_counter()
print(f"Solved the task in {toc-tic} sec")