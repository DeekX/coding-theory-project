import heapq
from collections import Counter
import numpy as np

def encode(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def average_bits_per_character(huffman_codes, frequency):
    total_symbols = sum(frequency.values())
    total_bits = sum(len(code)*freq for (_, code), freq in zip(huffman_codes, frequency.values()))
    return total_bits / total_symbols

probabilities = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
symbols = list(probabilities.keys())
probs = list(probabilities.values())

N = 100
sequence = np.random.choice(symbols, p=probs, size=N)

print("Generated sequence: ", ''.join(sequence))

frequency = Counter(sequence)
huffman_codes = encode(frequency)

huffman_dict = {symbol: code for symbol, code in huffman_codes}

encoded_sequence = ''.join(huffman_dict[symbol] for symbol in sequence)

NB = len(encoded_sequence) # Size of encoded sequence in bits
print(f"Size of encoded sequence (NB): {NB}")

compression_ratio = NB/(8*N) # Compression ratio
print(f"Compression ratio (NB/(8*N)): {compression_ratio}")

bits_per_symbol = NB/N # Number of bits per symbol
print(f"Number of bits per symbol (NB/N): {bits_per_symbol}")

avg_bits_per_character = average_bits_per_character(huffman_codes, frequency)
print(f"Average bits per character (Huffman): {avg_bits_per_character}")

# For ASCII, each character is 8 bits
ascii_bits = N * 8
print(f"Bits needed to encode the sequence with ASCII: {ascii_bits}")
