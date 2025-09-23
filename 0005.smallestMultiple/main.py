'''
Author: John Zoki
Smallest multiple
Problem 5:
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Answer: 232792560
Completed on Mon, 2 Aug 2021, 16:04
'''

import time

tic=time.perf_counter()

n = 2520
d = 2
d20 = False
while d20 == False:
	n += 1
	d = 2
	if n % d == 0:
		d += 1
		if n % d == 0:
			d += 1
			if n % d == 0:
				d += 1
				if n % d == 0:
					d += 1
					if n % d == 0:
						d += 1
						if n % d == 0:
							d += 1
							if n % d == 0:
								d += 1
								if n % d == 0:
									d += 1 #10
									if n % d == 0:
										d += 1
										if n % d == 0:
											d += 1
											if n % d == 0:
												d += 1
												if n % d == 0:
													d += 1
													if n % d == 0:
														d += 1
														if n % d == 0:
															print(f"{n} % {d} == True")
															d += 1
															if n % d == 0:
																print(f"{n} % {d} == True")
																d += 1
																if n % d == 0:
																	print(f"{n} % {d} == True")
																	d += 1
																	if n % d == 0:
																		print(f"{n} % {d} == True")
																		d += 1
																		if n % d == 0:
																			print(f"{n} % {d} == True")
																			d += 1
																			if n % d == 0:
																				d20 = True
print(f"Ergebnis: {n} % 20 == True!")

toc=time.perf_counter()
print(f"Solved the task in {toc-tic} sec")