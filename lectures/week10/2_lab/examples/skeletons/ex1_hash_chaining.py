# === Ex 1: Hash Table with Chaining ===
# Week 10 Hash Tables - Collision resolution using chaining (linked lists)
# Each bucket is implemented as a list, storing multiple items in the same bucket on collision
# Time complexity: Average O(1), Worst O(n) (when all keys hash to the same bucket)
# Space complexity: O(n + m) - n is the number of stored items, m is the table size
"""Hash Table with Chaining."""


class HashTableChaining:
    """Hash table using chaining for collision resolution.

    Collision resolution: keys with the same hash value are stored in a list (chain)
    Load factor = number of stored items / table size
    As the load factor increases, chains get longer and performance degrades
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize each bucket as an empty list
        self.count = 0  # Track the number of stored items

    def _hash(self, key):
        """Hash function: converts a key to a table index.

        Uses Python's built-in hash() followed by modulo with the table size
        Result: an index in the range 0 to (size-1)
        """
        return hash(key) % self.size

    def put(self, key, value):
        """Insert a key-value pair into the hash table.

        Algorithm:
        1. Compute the bucket index using the hash function
        2. Traverse the chain in that bucket to check if the same key exists
        3. If the same key exists, update the value (overwrite)
        4. If not, append a new item to the end of the chain

        Time complexity: Average O(1 + alpha), alpha = load factor
        """
        # TODO: Compute the bucket index using self._hash(key)
        # TODO: Traverse self.table[idx] to check if the key already exists
        #       If found, update the value: self.table[idx][i] = (key, value) and return
        # TODO: If key is new, append (key, value) to the chain and increment self.count
        pass  # TODO: implement

    def get(self, key):
        """Return the value for a key. Returns None if not found.

        Algorithm:
        1. Compute the bucket index using the hash function
        2. Traverse the chain in that bucket to search for the key

        Time complexity: Average O(1 + alpha), alpha = load factor
        """
        # TODO: Compute the bucket index using self._hash(key)
        # TODO: Traverse the chain and return the value if the key is found
        # TODO: Return None if the key is not found
        pass  # TODO: implement

    def delete(self, key):
        """Delete a key-value pair from the hash table.

        Algorithm:
        1. Compute the bucket index using the hash function
        2. Find and remove the key from the chain in that bucket

        Time complexity: Average O(1 + alpha)
        Returns: True if deletion succeeded, False if key not found
        """
        # TODO: Compute the bucket index using self._hash(key)
        # TODO: Find the key in the chain and remove it using pop(i)
        # TODO: Decrement self.count and return True on success
        # TODO: Return False if key not found
        pass  # TODO: implement

    def load_factor(self):
        """Return the load factor.

        Load factor = number of stored items / table size
        If the load factor exceeds 1, on average each bucket has more than one item
        Typically, resizing is considered when the load factor exceeds 0.75
        """
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableChaining(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    # Insert items and observe load factor changes
    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    # Search test
    print(f"\nget('cherry') = {ht.get('cherry')}")  # Existing key
    print(f"get('fig') = {ht.get('fig')}")          # Non-existing key

    # View internal bucket structure - visually inspect chaining state
    print("\nInternal table:")
    for i, bucket in enumerate(ht.table):
        print(f"  [{i}]: {bucket}")
