
import numpy as np

def setup(n):
    inputA_new = []
    inputB_new = []
    indexes = []
    for idx in range(0, n):
        inputA_new.append(np.random())
        inputB_new.append(np.random())
        indexes.append(idx)
    return inputA_new, inputB_new, indexes


def solve(inputA, inputB):
    inputA_new, inputB_new, indexes = [], [], []
    if len(inputA) == len(inputB):
        inputA_new, inputB_new, indexes = setup(len(inputA))
        while inputA is not inputB:
            for a, b, idx in zip(inputA, inputB, indexes):
                dice = np.random(0,1)
                if dice == 0:
                    a += 1
                    b -= 1
                else:
                    a -= 1
                    b += 1
                inputA_new[idx] = a
                inputB_new[idx] = b
    return inputA_new == inputB_new


num_of_cases = int(input())

for i in range(0, num_of_cases):
    n = int(input())
    inputA = [int(x) for x in input().split()]
    inputB = [int(x) for x in input().split()]
    solve(inputA, inputB)
