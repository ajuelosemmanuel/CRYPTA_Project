from .utils import modexp_rl

class TotallySafePRNG:
    """
    Implementation of the PRNG, without any logging or getter.
    """
    def __init__(self, seed):
        self.__seed = seed  # Here, we use this "__" syntax to prevent the use of the "__getattribute__" method, therefore making the PRNG a bit more secure.
        self.__counter = 0
   
    def get_Y(self) -> int:
        """
        Generates the next Y.

        Returns:
            int: random number between 0 and 255
        """
        self.__counter += 1
        optimization = modexp_rl((2**61 - 1), self.__counter, (2**127 - 1))
        return (self.__seed * optimization  % (2**127 - 1)) % (2**8)