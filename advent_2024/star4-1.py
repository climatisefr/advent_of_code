#!/usr/bin/python3
import starutils
import re


lines = starutils.startTest()

xmas = "XMAS"

total = 0
for idx, line in enumerate(lines):
	for pos in range(0, len(line)):
		if line[pos] == 'X':
			results = [ 1 for _ in range(8)]
			for n in range(1, 4):
				# Horiz forward
				if pos+n >= len(lines[idx]) or lines[idx][pos + n] != xmas[n]:
					results[0] = 0
				# Horiz back
				if pos-n < 0 or lines[idx][pos - n] != xmas[n]:
					results[1] = 0
				# Vert forward
				if idx+n >= len(lines) or lines[idx+n][pos] != xmas[n]:
					results[2] = 0
				# Vert back
				if idx-n < 0 or lines[idx-n][pos] != xmas[n]:
					results[3] = 0

				# diag up right
				if idx-n < 0 or pos+n >= len(lines[idx]) or lines[idx-n][pos+n] != xmas[n]:
					results[4] = 0
				# diag down right
				if idx+n >= len(lines) or pos+n >= len(lines[idx]) or lines[idx+n][pos+n] != xmas[n]:
					results[5] = 0
				# diag down left
				if idx+n >= len(lines) or pos-n < 0 or lines[idx+n][pos-n] != xmas[n]:
					results[6] = 0
				# diag up left
				if idx-n < 0 or pos-n < 0 or lines[idx-n][pos-n] != xmas[n]:
					results[7] = 0
			if sum(results) != 0:
				print(f"{idx}, {pos} => {sum(results)} {results}")
			total += sum(results)

print(total)
