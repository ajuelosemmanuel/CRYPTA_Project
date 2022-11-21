from fpylll import *
from ast import literal_eval

n = 21

def egcd(a, b):
    # Source : https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    # Source : https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gen_matrix(a:int, modulus:int, size:int) -> list:
    """
    Application directe de ce qui est écrit dans le cours.
    """
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        matrix[0][i] = pow(a, i, modulus)
    for i,j in zip(range(1,size), range(1,size)):
        if i==j:
            matrix[i][j] = modulus
    return matrix

def main(a:int, p:int, Ys:list):
    I = modinv(2**8, p)
    y = [ (el*I) % p for el in Ys]
    L = IntegerMatrix.from_matrix(gen_matrix(a, p, n))
    reduced = LLL.reduction(L)
    Xi_I = CVP.closest_vector(reduced, y, method="fast")
    Xi = [xi_i*2**8 % p for xi_i in Xi_I]
    inv_a = modinv(a, p)
    probable_seed = Xi[0] * inv_a % p
    probable_ys = [probable_seed * pow(a,i,p) % p % 2**8 for i in range(1,len(Ys)+1)]
    if probable_ys == Ys:
        print("Seed recovery complete")
        print("Seed : " + str(probable_seed))
    else:
        print("Not enough information to recover the seed.")

if __name__ == "__main__":
    a = int(input("a : "))
    p = int(input("p : "))
    Ys = literal_eval(input("Ys : "))
    main(a, p, Ys)

# a : 150879928588932929063915567870431524202
# p : 170141183460469231731687303715884105727
# Ys : [244, 73, 77, 149, 250, 28, 117, 8, 9, 178, 104, 0, 17, 136, 153, 54, 219, 253, 72, 219, 153]
# Seed recovery complete
# Seed : 46006708213540093617449443081394574359