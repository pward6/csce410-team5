import random
from compression.vByte import *
from compression.bitPacking import *


def generate_uniform_small(n=10000, max_val=10):
    return [random.randint(0, max_val) for _ in range(n)]


def generate_clustered(n=10000, base=1000, noise=5):
    return [base + random.randint(0, noise) for _ in range(n)]


def generate_sparse_with_outliers(n=10000):
    data = []
    for _ in range(n):
        if random.random() < 0.95:
            data.append(random.randint(1, 5))
        else:
            data.append(random.randint(1000, 100000))
    return data


def generate_monotonic_gaps(n=10000):
    pos = 0
    result = []
    for _ in range(n):
        gap = random.randint(1, 5)
        pos += gap
        result.append(pos)
    return result

def test_dataset(name, data):
    print(f"\n=== {name} ===")

    vbyte = VByteEncoder.encode_sequence(data)
    bitpack = BitPackEncoder.encode_sequence(data)

    print(f"vByte size: {len(vbyte):,}")
    print(f"BitPack size: {len(bitpack):,}")

    if len(vbyte) < len(bitpack):
        print("→ vByte wins")
    else:
        print("→ BitPack wins")

def run_all_tests():
    test_dataset("Uniform Small", generate_uniform_small())
    test_dataset("Clustered", generate_clustered())
    test_dataset("Sparse w/ Outliers", generate_sparse_with_outliers())
    test_dataset("Monotonic Gaps", generate_monotonic_gaps())
