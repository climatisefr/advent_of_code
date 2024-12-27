#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getParam
import re
import sys
import copy
import math
import time
from functools import cache

lines = startTest()
total = 0

for idx, line in enumerate(lines):
	total += 1

print(f"Step 1 total: {total}")