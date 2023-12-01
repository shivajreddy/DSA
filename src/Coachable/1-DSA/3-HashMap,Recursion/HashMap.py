"""
HashMaps
"""

'''
Hashing Technique

Open Hashing:
    -> Chaining

Closed Hashing:
    -> Open Addressing
        1. Linear Probing
        2. Quadratic Probing
        3. Double Hashing
'''


class Bucket:
    BUCKET = []

    def __init__(self):
        self.BUCKET = []

    def update(self, key: int, val: int) -> None:
        found = False
        for idx, kv in enumerate(self.BUCKET):
            if kv[0] == key:
                found = True
                self.BUCKET[idx] = (key, val)
                break
        if not found:
            self.BUCKET.append((key, val))

    def get(self, key: int) -> int:
        for (k, v) in self.BUCKET:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for idx, kv in enumerate(self.BUCKET):
            if kv[0] == key:
                del self.BUCKET[idx]


class MyHashMap:
    M = 2069
    HASH_TABLE = []

    def __init__(self):
        self.HASH_TABLE = [Bucket() for _ in range(self.M)]

    def put(self, key: int, value: int) -> None:
        hash_value = key % self.M
        self.HASH_TABLE[hash_value].update(key, value)

    def get(self, key: int) -> int:
        hash_value = key % self.M
        return self.HASH_TABLE[hash_value].get(key)

    def remove(self, key: int) -> None:
        hash_value = key % self.M
        self.HASH_TABLE[hash_value].remove(key)
