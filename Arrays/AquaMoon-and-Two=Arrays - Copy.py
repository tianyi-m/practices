import numpy as np

def setup(n):
    inputA_new = np.random.rand(0, n)
    inputB_new = np.random.rand(0, n)
    indexes = np.random.rand(0, n)
    return inputA_new, inputB_new, indexes


def solve(inputA, inputB):
    inputA_new, inputB_new, indexes = [], [], []
    if len(inputA) == len(inputB):
        inputA_new, inputB_new, indexes = setup(len(inputA))
        while inputA is not inputB:
            for a, b, idx in zip(inputA, inputB, indexes):
                    a += 1
                    b += 1
                inputA_new[idx] = a
                inputB_new[idx] = b
    return inputA_new == inputB_new


seed = int(input)
luck = int(input)
score = 0
ending = False

while ending != True:
    inputA = [int(x) for x in input().split()]
    inputB = [int(x) for x in input().split()]
    while ending != True:
        progress = input()
        score += progress
        solution = solve(inputA, inputB)

print("expectation:", seed, "score: ", score, "Result:  ", True)
