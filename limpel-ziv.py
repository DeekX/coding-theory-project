import numpy as np
import math
from collections import defaultdict

def entropy(probabilities):
    return -sum([p*math.log2(p) for p in probabilities])

def lempel_ziv_encoding(sequence):
    i = 0
    dictionary = defaultdict(int)
    output = []
    while i < len(sequence):
        phrase = sequence[i]
        while phrase in dictionary and i < len(sequence):
            i += 1
            if i < len(sequence):
                phrase += sequence[i]
        output.append(phrase)
        dictionary[phrase] = len(dictionary) + 1
        i += 1
    return output

probabilities = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
symbols = list(probabilities.keys())
probs = list(probabilities.values())

N = 100
NB_values = []

for _ in range(5):
    sequence = np.random.choice(symbols, p=probs, size=N)
    print(f"Generated sequence: {''.join(sequence)}")

    print(f"Source entropy: {entropy(probs)} bits")

    encoded_sequence = lempel_ziv_encoding(''.join(sequence))
    print(f"Lempel-Ziv Encoded Sequence: {encoded_sequence}")

    NB = len(encoded_sequence) * math.ceil(math.log2(len(encoded_sequence) + 1)) + len(encoded_sequence) * 8
    NB_values.append(NB)

    print(f"Number of binary digits needed to encode the sequence: {NB}")
    print(f"Bits per symbol: {NB/N}")

average_NB = sum(NB_values) / len(NB_values)
print(f"Average number of binary digits needed to encode the sequences: {average_NB}")

compression_ratio = average_NB / (N*8)
print(f"Compression ratio relative to the ASCII code: {compression_ratio}")
