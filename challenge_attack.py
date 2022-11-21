from fpylll import *
from challenge.challenge import *

n = 19  # D'après https://hal.archives-ouvertes.fr/hal-02700791/document page 8, il suffit de 63 Y consécutifs pour retrouver la graine utilisée - ici, après divers tests, il s'avère qu'il nous faut que 19 Y_i consécutifs pour retrouver les X_i correspondants.

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

# Voir les explications dans le rapport
I = modinv(2**8, p)

y = [ (el*I) % p for el in Y[:-46]]  # On prend soin de ne garder que les 19 premières valeurs

L = IntegerMatrix.from_matrix(gen_matrix(a, p, n))
reduced = LLL.reduction(L)
Xi_I = CVP.closest_vector(reduced, y, method="fast")

# Nous avons maintenant les 63 premiers X_i multipliés par I (cf rapport)
# Il est alors possible de prédire tous les Y_i suivants

Xi = [xi_i*2**8 % p for xi_i in Xi_I]

# Nous tentons maintenant de retrouver une seed potentielle
inv_a = modinv(a, p)

probable_seed = Xi[0] * inv_a % p

# Vérification

probable_ys = [probable_seed * pow(a,i,p) % p % 2**8 for i in range(1,66)]

if probable_ys == Y:
    print("Seed recovery complete")
    print("Seed : " + str(probable_seed))
else:
    print("Not enough information to recover the seed.")