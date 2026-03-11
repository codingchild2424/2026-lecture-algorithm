# === A-3: Huffman Coding ===
# Optimal prefix code generation using the greedy algorithm
#
# Key concepts:
# - Greedy strategy: Merge the two nodes with the lowest frequency at each step
# - Uses a min-heap (priority queue) for efficient minimum extraction
# - Higher frequency characters get shorter codes -> minimizes total bits
# - Prefix code property: No code is a prefix of another -> decoding without delimiters
# - Time complexity: O(n log n) (n = number of distinct characters, n-1 heap operations)
# - Space complexity: O(n) (number of tree nodes)
"""
Huffman Coding Implementation

Greedy strategy: Repeatedly merge the two nodes with the lowest frequency
to generate an optimal prefix code.

Implementation details:
1. Build frequency table
2. Build Huffman tree using a min-heap
3. Generate codes (tree traversal)
4. Encoding / Decoding
5. Compression ratio calculation
"""

import heapq
import math
from collections import Counter


class HuffmanNode:
    """A node in the Huffman tree."""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char      # Character of leaf node (None for internal nodes)
        self.freq = freq      # Frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        """Compare by frequency for the min-heap."""
        return self.freq < other.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def build_frequency_table(text):
    """Calculate the character frequency of the text.

    Args:
        text: Input string

    Returns:
        {character: frequency} dictionary (sorted by frequency descending)
    """
    return dict(Counter(text).most_common())


def build_huffman_tree(freq_table):
    """Build a Huffman tree from the frequency table.

    Greedy choice: Merge the two nodes with the lowest frequency at each step.

    Args:
        freq_table: {character: frequency} dictionary

    Returns:
        Root node of the Huffman tree
    """
    # Create a leaf node for each character and insert into the min-heap
    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))

    # Handle case with only one unique character
    if len(heap) == 1:
        node = heapq.heappop(heap)
        root = HuffmanNode(freq=node.freq, left=node)
        return root

    # Merge the two smallest nodes until only one remains
    step = 0
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node
        merged = HuffmanNode(
            freq=left.freq + right.freq,
            left=left,
            right=right,
        )
        heapq.heappush(heap, merged)

        step += 1
        left_label = repr(left.char) if left.is_leaf() else f"[{left.freq}]"
        right_label = repr(right.char) if right.is_leaf() else f"[{right.freq}]"
        print(f"    Step {step}: merge {left_label}({left.freq}) + "
              f"{right_label}({right.freq}) = [{merged.freq}]")

    return heapq.heappop(heap)


def generate_codes(root, prefix="", codes=None):
    """Traverse the Huffman tree to generate the code for each character.

    Left edge = '0', Right edge = '1'

    Args:
        root: Root node of the Huffman tree
        prefix: Code prefix built so far
        codes: Code dictionary (for recursive calls)

    Returns:
        {character: binary code string} dictionary
    """
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.is_leaf():
        # Leaf node -- code is finalized
        codes[root.char] = prefix if prefix else "0"
        return codes

    generate_codes(root.left, prefix + "0", codes)
    generate_codes(root.right, prefix + "1", codes)

    return codes


def encode(text, codes):
    """Encode the text using Huffman codes.

    Args:
        text: Original string
        codes: {character: binary code string} dictionary

    Returns:
        Encoded bit string
    """
    return "".join(codes[char] for char in text)


def decode(encoded_text, root):
    """Decode an encoded bit string using the Huffman tree.

    Args:
        encoded_text: Encoded bit string
        root: Root node of the Huffman tree

    Returns:
        Decoded string
    """
    decoded = []
    current = root

    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            decoded.append(current.char)
            current = root

    return "".join(decoded)


def print_tree(node, prefix="", is_left=True, is_root=True):
    """Visually print the Huffman tree."""
    if node is None:
        return

    if is_root:
        connector = ""
    elif is_left:
        connector = "|-- (0) "
    else:
        connector = "`-- (1) "

    if node.is_leaf():
        label = f"{repr(node.char)} [{node.freq}]"
    else:
        label = f"[{node.freq}]"

    print(f"    {prefix}{connector}{label}")

    if not is_root:
        new_prefix = prefix + ("|       " if is_left else "        ")
    else:
        new_prefix = prefix

    if not node.is_leaf():
        print_tree(node.left, new_prefix, True, False)
        print_tree(node.right, new_prefix, False, False)


def huffman_coding(text):
    """Perform the complete Huffman coding process.

    Args:
        text: String to encode

    Returns:
        (encoded bit string, Huffman code table, tree root)
    """
    # 1. Build frequency table
    print("\n  [Step 1] Build frequency table")
    freq_table = build_frequency_table(text)
    print(f"    {'Char':<8} {'Freq':>6} {'Ratio':>8}")
    print(f"    {'-'*24}")
    for char, freq in freq_table.items():
        ratio = freq / len(text) * 100
        print(f"    {repr(char):<8} {freq:>6} {ratio:>7.1f}%")

    # 2. Build Huffman tree
    print(f"\n  [Step 2] Build Huffman tree (greedy: merge 2 lowest-frequency nodes)")
    root = build_huffman_tree(freq_table)

    # Tree visualization
    print(f"\n  [Step 2-1] Huffman tree:")
    print_tree(root)

    # 3. Generate codes
    print(f"\n  [Step 3] Generate Huffman codes")
    codes = generate_codes(root)
    # Sort by code length
    sorted_codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))
    print(f"    {'Char':<8} {'Code':<15} {'Len':>4} {'Freq':>6}")
    print(f"    {'-'*36}")
    for char, code in sorted_codes:
        print(f"    {repr(char):<8} {code:<15} {len(code):>4} {freq_table[char]:>6}")

    # Prefix code verification
    print(f"\n  [Step 3-1] Prefix code verification:")
    is_prefix_free = True
    code_list = list(codes.values())
    for i in range(len(code_list)):
        for j in range(len(code_list)):
            if i != j and code_list[j].startswith(code_list[i]):
                is_prefix_free = False
                break
    print(f"    Prefix code property: {'PASS' if is_prefix_free else 'FAIL'}")

    # 4. Encoding
    print(f"\n  [Step 4] Encoding")
    encoded = encode(text, codes)
    text_display = repr(text[:80]) + ("..." if len(text) > 80 else "")
    print(f"    Original: {text_display}")
    display_encoded = encoded[:80]
    print(f"    Encoded: {display_encoded}{'...' if len(encoded) > 80 else ''}")

    # 5. Decoding verification
    print(f"\n  [Step 5] Decoding verification")
    decoded = decode(encoded, root)
    is_correct = decoded == text
    decoded_display = repr(decoded[:80]) + ("..." if len(decoded) > 80 else "")
    print(f"    Decoded result: {decoded_display}")
    print(f"    Matches original: {'PASS' if is_correct else 'FAIL'}")

    # 6. Compression ratio calculation
    print(f"\n  [Step 6] Compression ratio calculation")
    original_bits = len(text) * 8  # 8 bits per character (ASCII)
    encoded_bits = len(encoded)
    compression_ratio = (1 - encoded_bits / original_bits) * 100

    # Compare with fixed-length codes
    num_chars = len(freq_table)
    fixed_bits_per_char = math.ceil(math.log2(num_chars)) if num_chars > 1 else 1
    fixed_total_bits = len(text) * fixed_bits_per_char

    # Huffman average bits
    avg_huffman_bits = encoded_bits / len(text)

    # Entropy (theoretical lower bound)
    entropy = 0
    for freq in freq_table.values():
        p = freq / len(text)
        if p > 0:
            entropy -= p * math.log2(p)

    print(f"    Original size (ASCII 8bit):     {original_bits:>8} bits ({original_bits // 8} bytes)")
    print(f"    Fixed-length code ({fixed_bits_per_char}bit):    {fixed_total_bits:>8} bits")
    print(f"    Huffman coding:                 {encoded_bits:>8} bits")
    print(f"    Theoretical lower bound (H):    {len(text) * entropy:>8.0f} bits")
    print(f"")
    print(f"    Huffman avg bits/char:          {avg_huffman_bits:.3f}")
    print(f"    Entropy:                        {entropy:.3f}")
    print(f"    Compression vs ASCII:           {compression_ratio:.1f}%")
    print(f"    Compression vs fixed-length:    {(1 - encoded_bits / fixed_total_bits) * 100:.1f}%")

    return encoded, codes, root


if __name__ == "__main__":
    print("=" * 65)
    print(" Huffman Coding")
    print("=" * 65)

    # Example 1: Simple text
    print("\n" + "=" * 65)
    print("[Example 1] Simple text")
    print("=" * 65)

    text1 = "abracadabra"
    huffman_coding(text1)

    # Example 2: English sentence
    print("\n" + "=" * 65)
    print("[Example 2] English sentence")
    print("=" * 65)

    text2 = "the quick brown fox jumps over the lazy dog"
    huffman_coding(text2)

    # Example 3: Highly skewed frequency text
    print("\n" + "=" * 65)
    print("[Example 3] Highly skewed frequency text (high compression effect)")
    print("=" * 65)

    text3 = "aaaaaaaabbbbccdd"
    huffman_coding(text3)

    # Summary
    print("\n" + "=" * 65)
    print(" Summary")
    print("=" * 65)
    print("""
  Huffman coding greedy strategy:
  - At each step, merge the two nodes with the lowest frequency
  - This strategy is proven to generate optimal prefix codes

  Time complexity: O(n log n)
  - n = number of distinct characters
  - Heap operations (insert/delete) are O(log n), performed n-1 times

  Key properties:
  - Prefix code: No code is a prefix of another code
  - This enables decoding without delimiters
  - Higher frequency -> shorter code -> minimizes total bits
""")
