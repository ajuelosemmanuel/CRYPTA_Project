from lib.scheme_logging import TotallySafePRNG
from lib.utils import gen_seed
from fpylll import *

seed = gen_seed()
prng = TotallySafePRNG(seed)
while len(prng.get_Y_history()) != 65 :
    prng.get_next_Y()

Y_list = prng.get_Y_history()

n=65
m = pow(2,127) - 1
a = pow(2,61) - 1
mem = pow(2,119)

A = [[0]*n for i in range(n)]

for i in range(1,n):
    for j in range(1,n):
        if(i==j):
            A[i][j] = m
        A[0][j] = pow(a,i)

print("A = ", A)
y = [el * mem for el in Y_list]
print("y = ", y)
L = IntegerMatrix.from_matrix(A)
print("L = ", LLL.is_reduced(L))
v0 = CVP.closest_vector(L, y)
print(v0)