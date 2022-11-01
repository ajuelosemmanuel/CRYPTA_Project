class TotallySafePRNG:
    """
    Naive implementation of the PRNG, with getters and logging functions.
    Because this is a version of the class designed to run tests, it has NO security whatsoever.
    """
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
        self.x = seed
        self.x_history = [seed]
    
    def __str__(self):
        """
        Displays the seed, the current value of X and the number of numbers the PRNG has generated.
        """
        maniaque = "numbers" if (self.counter != 1) else "number"
        return f"Seed : {self.seed}\nCurrent X : {self.x}\nHas generated {self.counter} " + maniaque
    
    def get_Y(self):
        """
        Displays the current Y.

        Returns:
            int: random number between 0 and 255
        """
        self.counter += 1
        self.x = ((2**61 - 1) * self.x) % (2**127 - 1)
        self.x_history.append(self.x)
        return self.x % 2**8
    
    def get_X_history(self):
        """
        Returns a string containing all the values of X and their indices.
        """
        result:str = ""
        for count, value in enumerate(self.x_history):
            result += (f'X_{count}\t:\t' + "{:0127b}".format(value)) + "\n"
        return result

    def get_Y_history(self):
        """
        Returns a string containing all the values of Y and their indices.
        """
        result:str = ""
        for count, value in enumerate(self.x_history):
            if count != 0:
                result += (f'Y_{count}\t:\t' + "{:08b}".format(value)[-8:]) + "\n"
        return result