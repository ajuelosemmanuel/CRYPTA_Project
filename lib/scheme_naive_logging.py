class TotallySafePRNG:
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
        self.x = seed
        self.x_history = [seed]
    
    def __str__(self):
        maniaque = "numbers" if (self.counter != 1) else "number"
        return f"Seed : {self.seed}\nCurrent X : {self.x}\nHas generated {self.counter} " + maniaque
    
    def get_Y(self):
        self.counter += 1
        self.x = ((2**61 - 1) * self.x) % (2**127 - 1)
        self.x_history.append(self.x)
        return self.x % 2**8
    
    def get_X_history(self):
        for count, value in enumerate(self.x_history):
            print(f'X_{count}\t:\t' + "{:0127b}".format(value))

    def get_Y_history(self):
        for count, value in enumerate(self.x_history):
            if count != 0:
                print(f'Y_{count}\t:\t' + "{:08b}".format(value)[-8:])