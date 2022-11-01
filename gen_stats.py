import pickle as pkl
from tqdm import tqdm
from lib.utils import gen_seed
from lib.scheme import TotallySafePRNG

def generate_statistics():
    numbers = []
    for _ in tqdm(range(100)):
        seed = gen_seed()
        prng_tmp = TotallySafePRNG(seed)
        for _ in range(1000):
            numbers.append(prng_tmp.get_Y())
    with open("statistics/stats.pkl", "wb") as f:
        pkl.dump(numbers, f)

if __name__ == "__main__":
    generate_statistics()