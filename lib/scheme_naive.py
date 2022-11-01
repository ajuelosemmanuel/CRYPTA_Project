class TotallySafePRNG:
    """
    Naive implementation of the PRNG, without any logging or getter.
    """
    def __init__(self, seed):
        self.__seed = seed  # Here, we use this "__" syntax to prevent the use of the "__getattribute__" method, therefore making the PRNG a bit more secure.
        self.__x = seed
   
    def get_Y(self) -> int:
        """
        Generates the next Y.

        Returns:
            int: random number between 0 and 255
        """
        self.x = (2**61 - 1) * self.x % (2**127 - 1)
        return self.x % 2**8