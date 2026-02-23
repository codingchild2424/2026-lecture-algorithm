"""Hash Table with Chaining."""


class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.count += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                self.count -= 1
                return True
        return False

    def load_factor(self):
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableChaining(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    print(f"\nget('cherry') = {ht.get('cherry')}")
    print(f"get('fig') = {ht.get('fig')}")

    # Show internal structure
    print("\nInternal table:")
    for i, bucket in enumerate(ht.table):
        print(f"  [{i}]: {bucket}")
