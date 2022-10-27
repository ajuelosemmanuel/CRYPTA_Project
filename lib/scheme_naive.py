class TotallySafePRNG:
    def __init__(self, seed):
        self.seed = seed
        self.x = seed
   
    def get_Y(self):
        self.x = (2**61 - 1) * self.x % (2**127 - 1)
        return self.x % 2**8