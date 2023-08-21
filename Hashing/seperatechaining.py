class HashTable:
    
    def __init__(self) -> None:
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        self.table[hash_value].append((key, value))
        
    def search(self, key):
        hash_value = self.hash_function(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                return item[1]
        return None