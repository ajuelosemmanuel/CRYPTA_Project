import random

def modexp_rl(a:int, b:int, n:int) -> int:
    """
    Optimized modular exponentiation function.
    """
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b >>= 1
        if b == 0:
            break
        a = a * a % n
    return r

def gen_seed() -> int:
    """
    Generates a 127bits integer, which can be used as a seed for the PRNG.
    """
    return random.getrandbits(127)