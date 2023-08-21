class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def hash_func(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_value = self.hash_func(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, value)
        else:
            i = 1
            while True:
                new_hash = (hash_value + i) % self.size
                if self.table[new_hash] is None:
                    self.table[new_hash] = (key, value)
                    break
                elif i > self.size:
                    if i < self.table[hash_value][2]:
                        self.table[hash_value], self.table[new_hash] = self.table[new_hash], self.table[hash_value]
                    break
                elif self.table[new_hash][0] == key:
                    self.table[new_hash] = (key, value, i)
                    break
                elif self.table[new_hash][2] < i:
                    self.table[hash_value], self
