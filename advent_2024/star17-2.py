#!/usr/bin/python3
from starutils import printD

expected_lst = [2, 4, 1, 1, 7, 5, 1, 4, 0, 3, 4, 5, 5, 5, 3, 0]


def form_values(value, possible, idx):
	result = list()
	ref = value&127
	#print(f"form_values idx: {idx} ref: 0x{ref:x} value: {value}")
	if idx >= len(possible):
		#print(f"Value: {value}")
		if value not in result:
			result.append(value)
		return result
	value <<= 3
	for p in possible[idx]:
		#print(f"p: 0x{p:x} p>>3: {p>>3:x} ref: 0x{ref:x}")
		if ((p>>3)&127) == ref:
			r = form_values(value + (p & 7), possible, idx+1)
			for rr in r:
				if rr not in result:
					result.append(rr)
	return result


def backward(lst):
	rev = lst[:]
	rev.reverse()

	A = 0
	possible = list()
	possible.append([0])
	for idx, i in enumerate(rev):
		possible.append([])
		pp = list()
		for j in possible[idx]:
			if (j&127) not in pp:
				pp.append(j&127)
		for A in range(1024):
			if (A >> 3) not in pp:
				continue
			alpha = (A & 0x7) ^ 1 # 0 to 7
			B = alpha ^ 4 ^ (A >> alpha)
			if B & 0x7 == i:
				printD(f"{idx} A: 0x{A:x} A&127: {A&127:x} A>>3: 0x{A>>3:x} / B: 0x{B:x} : B%8: {B&7} ")
				possible[-1].append(A)
		printD(f"possible[-1]: {', '.join([f'{x:x}' for x in possible[-1]])}")
		printD("===================")

	result = list()
	for start_val in possible[-1]:
		res = form_values(0, possible, 0)
		for r in res:
			if r not in result:
				result.append(r)
	return result

def forward(A):
	output = list()
	while A != 0:
		alpha = (A & 0x7) ^ 1 # 0 to 7
		B = alpha ^ 4 ^ (A >> alpha)
		output.append(B & 0x7)
		A >>= 3
	return output

sol = backward(expected_lst)
sol.sort()
printD(f"sol: {sol}")
verif = forward(sol[0])
printD(f"verif: {verif}")
print(f"Step 2 output: {sol[0]}")
