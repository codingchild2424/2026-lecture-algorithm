"""Hash Table with Linear Probing (Open Addressing)."""


class HashTableProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")
        idx = self._hash(key)
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size
        if self.keys[idx] is None:
            self.count += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None

    def load_factor(self):
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableProbing(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    print(f"\nget('cherry') = {ht.get('cherry')}")

    print("\nInternal table:")
    for i in range(ht.size):
        print(f"  [{i}]: key={ht.keys[i]}, value={ht.values[i]}")
