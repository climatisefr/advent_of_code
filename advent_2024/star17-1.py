#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getParam
import re
import sys

lines = startTest()
total = 0

output = list()
reg = [0, 0, 0]
PC = 0
instructions = list()

for idx,line in enumerate(lines):
	m = re.match("Register (.): (\d+)", line)
	if m:
		reg2idx = {'A': 0, 'B': 1, 'C': 2}
		reg[reg2idx[m.group(1)]] = int(m.group(2))
	m = re.match("Program: ([0-7,]+)", line)
	if m:
		instructions = [int(x) for x in m.group(1).split(',')]

def combo_val(lit):
	if lit < 4:
		return lit
	if lit < 7:
		return reg[lit-4]
	if lit == 7:
		print(f"Error Combo with lit: {lit}")
		sys.exit(-1)

def combo_str(lit):
	if lit < 4:
		return lit
	if lit < 7:
		return {0: "A", 1: "B", 2: "C"}[lit-4]
	if lit == 7:
		print(f"Error Combo with lit: {lit}")
		sys.exit(-1)

printD(f"Registers: {reg}, instructions {instructions}")

for i in range(0, len(instructions), 2):
	inst = instructions[i]
	op = instructions[i+1]
	if inst in [0, 6, 7]: # adv, bdv, cdv
		inst2out = {0: "A", 6: "B", 7: "C"}
		printD(f"{i}: {inst2out[inst]} = A / {combo_str(op)}")
	if inst in [1, 4]: # bxl, bxc
		val = str(op)
		if inst == 4:
			val = "C"
		printD(f"{i}: B = B ^ {val}")
	if inst == 2: # bst
		printD(f"{i}: B = {combo_str(op)} % 8")
	if inst == 3: #jnz
		printD(f"{i}: jnz (A!=0) {op}")
	if inst == 5: # out
		printD(f"{i}: output {combo_str(op)} % 8")

while PC < len(instructions):
	inst = instructions[PC]
	op = instructions[PC+1]
	printD(f"PC {PC}, inst: {inst}, op: {op}")
	if inst in [0, 6, 7]: # adv, bdv, cdv
		denom = 1 << combo_val(op)
		inst2out = {0: 0, 6: 1, 7: 2}
		reg[inst2out[inst]] = int(reg[0] / denom)
		PC += 2
	if inst in [1, 4]: # bxl, bxc
		val = op
		if inst == 4:
			val = reg[2]
		reg[1] = reg[1] ^ val
		PC += 2
	if inst == 2: # bst
		reg[1] = (combo_val(op)) & 0x7
		PC += 2
	if inst == 3: #jnz
		if reg[0] != 0:
			PC = op
		else:
			PC += 2
	if inst == 5: # out
		output.append(combo_val(op) & 0x7)
		PC += 2


print(f"Step 1 output: {','.join([str(x) for x in output])}")