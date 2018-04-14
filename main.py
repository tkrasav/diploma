import os
import sys

sys.path.append(os.getcwd())

import structure

arr = structure.parse('res/current.json')
print(arr)
