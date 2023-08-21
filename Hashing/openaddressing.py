class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.table = [None] * self.size
        
    def hash_func(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_value = self.hash_func(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = [(key, value)]
            
        else:
            i =1
            while True:
                new_hash = (hash_value + i) % self.size
                if self.table[new_hash] is None:
                    self.table[new_hash] = [(key, value)]
                    break
                i += 1
                if i == self.size:
                    raise Exception('Hash table is full')
                
    def search(self, key):
        hash_value = self.hash_func(key)
        if self.table[hash_value] is None:
            return None
        elif self.table[hash_value][0] == key:
            return self.table[hash_value][1]
        else:
            i = 1
            while True:
                new_hash = (hash_value + i) % self.size
                if self.table[new_hash] is None:
                    return None
                elif self.table[new_hash][0] == key:
                    return self.table[new_hash][1]
                i += 1
                if i == self.size:
                    return None
                
                