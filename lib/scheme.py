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
        return self.__seed * optimization  % (2**127 - 1)