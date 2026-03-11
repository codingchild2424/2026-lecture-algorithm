# === Ex 2: Hash Table with Linear Probing ===
# Week 10 Hash Tables - Linear probing, a type of open addressing
# On collision, sequentially search for the next empty slot
# Time complexity: Average O(1/(1-alpha)), Worst O(n) - alpha is the load factor
# Space complexity: O(m) - m is the table size (no extra lists unlike chaining)
"""Hash Table with Linear Probing (Open Addressing)."""


class HashTableProbing:
    """Hash table using linear probing.

    Open Addressing: all items are stored directly within the table
    Linear Probing: on collision, probe h(k), h(k)+1, h(k)+2, ... for an empty slot
    Clustering problem: consecutive filled slots increase search time (primary clustering)
    Performance degrades sharply as the load factor approaches 1
    """
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size    # Key array (None means empty slot)
        self.values = [None] * size  # Value array
        self.count = 0               # Number of stored items

    def _hash(self, key):
        """Hash function: converts a key to a table index.

        Uses Python's built-in hash() followed by modulo with the table size
        Result: an index in the range 0 to (size-1)
        """
        return hash(key) % self.size

    def put(self, key, value):
        """Insert a key-value pair into the hash table.

        Algorithm:
        1. Compute the initial index using the hash function
        2. If the slot is not empty and contains a different key,
           move to the next slot (linear probing: idx = (idx + 1) % size)
        3. When an empty slot or a slot with the same key is found, store the value

        Time complexity: Average O(1/(1-alpha)), raises exception if table is full
        """
        # TODO: Raise an Exception if self.count >= self.size (table full)
        # TODO: Compute initial index using self._hash(key)
        # TODO: Linear probing loop: while self.keys[idx] is not None and self.keys[idx] != key,
        #       advance idx = (idx + 1) % self.size
        # TODO: If self.keys[idx] is None, increment self.count (new key)
        # TODO: Store key and value in self.keys[idx] and self.values[idx]
        pass  # TODO: implement

    def get(self, key):
        """Return the value for a key. Returns None if not found.

        Algorithm:
        1. Compute the initial index using the hash function
        2. Search for the key using linear probing
        3. If an empty slot is encountered, the key does not exist (stop search)
        4. If we wrap around to the starting position, the key does not exist

        Time complexity: Average O(1/(1-alpha))
        """
        # TODO: Compute initial index using self._hash(key)
        # TODO: Record start position for wrap-around detection
        # TODO: Linear probing loop: while self.keys[idx] is not None,
        #       check if self.keys[idx] == key (return value if found)
        #       advance idx = (idx + 1) % self.size
        #       break if idx == start (full loop)
        # TODO: Return None if not found
        pass  # TODO: implement

    def load_factor(self):
        """Return the load factor.

        In open addressing, the load factor can never exceed 1 (limited by table size)
        Typically, resizing should be considered when the load factor exceeds 0.5-0.7
        """
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableProbing(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    # Insert items and observe load factor changes
    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    # Search test
    print(f"\nget('cherry') = {ht.get('cherry')}")

    # View internal table structure - observe clustering caused by linear probing
    print("\nInternal table:")
    for i in range(ht.size):
        print(f"  [{i}]: key={ht.keys[i]}, value={ht.values[i]}")
