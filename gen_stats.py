import pickle as pkl                            # To save my list
from tqdm import tqdm                           # Clean display !
from lib.utils import gen_seed                  # Seed generator
from lib.actual_scheme import TotallySafePRNG   # The PRNG

# Note : I can't find a way to run it in the statistics folder, as I couldn't import stuff from a sibling folder on Windows...

def generate_statistics():
    """
    Creates a list of numbers generated by the PRNG using different seeds and saves it in a pickle file.
    """
    numbers = []
    for _ in tqdm(range(1000)):
        seed = gen_seed()
        a = gen_seed()
        prng_tmp = TotallySafePRNG(a, seed)
        for _ in range(10000):
            numbers.append(prng_tmp.get_Y())
    with open("statistics/stats.pkl", "wb") as f:
        pkl.dump(numbers, f)

if __name__ == "__main__":              # Make it a script
    generate_statistics()