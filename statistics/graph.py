import sys
sys.path.append("..")                   # Go back to the previous folder to fix directory issue
from lib.utils import gen_seed          # Seed generator
from lib.scheme import TotallySafePRNG  # The PRNG
from matplotlib import pyplot as plt    # To plot simple 2D graphs

def generate_statistics():
    """
    Creates a list of numbers generated by the PRNG using different seeds and saves it in a pickle file.
    """
    for i in range(3):                  # For 3 seeds
        numbers = []
        occurrences = []
        seed = gen_seed()
        prng_tmp = TotallySafePRNG(seed)
        for z in range(1000):           # Generate 1000 Y
            numbers.append(prng_tmp.get_Y())
        for j in range(256):            # The numbers are on 8 bits so they will be between 0 and 255
            occurrences.append(numbers.count(j))
        plt.plot(occurrences, "C"+str(i), label="seed ="+str(seed))
    plt.legend()
    plt.show()                          # Print the graph of occurrences for each number

if __name__ == "__main__":              # Make it a script
    generate_statistics()
