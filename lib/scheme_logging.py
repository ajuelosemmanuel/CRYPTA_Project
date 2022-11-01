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

class TotallySafePRNG:
    """
    Implementation of the PRNG, with getters and logging functions.
    Because this is a version of the class designed to run tests, it has NO security whatsoever.
    """
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0

    def get_X(self,i:int) -> int:
        """
        Displays X for a given i.

        Returns:
            int: value of X
        """
        optimization = modexp_rl((2**61 - 1), i, (2**127 - 1))
        return self.seed * optimization  % (2**127 - 1)

    def get_Y(self):
        """
        Displays the current Y.

        Returns:
            int: random number between 0 and 255
        """
        return self.get_X(self.counter) % 2**8

    def get_next_Y(self):
        """
        Generates the next Y.

        Returns:
            int: random number between 0 and 255
        """
        self.counter += 1
        return self.get_Y()
    
    def __str__(self) -> str:
        """
        Displays the seed and the number of numbers the PRNG has generated.
        """
        maniaque = "numbers" if (self.counter != 1) else "number"
        return f"Seed : {self.seed}\nHas generated {self.counter} " + maniaque
    
    def get_X_history(self) -> str:
        """
        Returns a string containing all the values of X and their indices.
        """
        result:str = ""
        for i in range(self.counter):
            result += (f'X_{i}\t:\t' + "{:0127b}".format(self.get_X(i))) + "\n"
        return result

    def get_Y_history(self) -> str:
        """
        Returns a string containing all the values of Y and their indices.
        """
        result:str = ""
        for i in range(self.counter):
            if i!= 0:
                result += (f'Y_{i}\t:\t' + "{:08b}".format(self.get_X(i) % 2**8)) + "\n"
        return result