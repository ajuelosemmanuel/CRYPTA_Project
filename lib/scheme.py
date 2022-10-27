def modexp_rl(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b >>= 1
        if b == 0:
            break
        a = a * a % n
    return r

class TotallySafePRNG:
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
   
    def get_Y(self):
        self.counter += 1
        optimization = modexp_rl((2**61 - 1), self.counter, (2**127 - 1))
        return self.seed * optimization  % (2**127 - 1)