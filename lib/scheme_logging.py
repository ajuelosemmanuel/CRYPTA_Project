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

    def X_from_i(self,i):
        optimization = modexp_rl((2**61 - 1), i, (2**127 - 1))
        return self.seed * optimization  % (2**127 - 1)

    def get_Y(self):
        self.counter += 1
        return self.X_from_i(self.counter) % 2**8
    
    def __str__(self):
        maniaque = "numbers" if (self.counter != 1) else "number"
        return f"Seed : {self.seed}\nHas generated {self.counter} " + maniaque
    
    def get_X_history(self):
        for i in range(self.counter):
            print(f'X_{i}\t:\t' + "{:0127b}".format(self.X_from_i(i)))

    def get_Y_history(self):
        for i in range(self.counter):
            print(f'X_{i}\t:\t' + "{:0127b}".format(self.X_from_i(i) % 2**8))