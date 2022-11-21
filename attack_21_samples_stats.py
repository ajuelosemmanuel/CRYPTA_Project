from fpylll import *
from lib.actual_scheme import TotallySafePRNG
from lib.utils import gen_seed

n = 21  # D'après https://hal.archives-ouvertes.fr/hal-02700791/document page 8, il suffit de 63 Y consécutifs pour retrouver la graine utilisée.

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
        return probable_seed
    else:
        return -1

if __name__ == "__main__":
    p = pow(2,127)-1
    cpt = 0
    for i in range(10000):
        a = gen_seed()
        seed = gen_seed()
        prng = TotallySafePRNG(a, seed)
        samples = [prng.get_Y() for i in range(n)]
        result = main(a, p, samples)
        if result == seed:
            cpt+=1
    print("Pourcentage de réussite : " + str((cpt*100)/10000))