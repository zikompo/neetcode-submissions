class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

def q_hash(key, capacity, i):
        return (primary_hash(key, capacity) + i)%capacity

def primary_hash(key,capacity):
    return key%capacity

class HashTable:
    
    def __init__(self, capacity: int):
        self.hash = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        # using quadratic hashing
        index_to_insert = primary_hash(key, self.capacity)
        if self.hash[index_to_insert] == None:
            self.hash[index_to_insert] = Node(key, value)
            self.size += 1
            self.check_load_factor()
        elif self.hash[index_to_insert].key == key:
            self.hash[index_to_insert].value = value
        else:
            i = 1
            while self.hash[q_hash(key, self.capacity, i**2)] != None:
                x = self.hash[q_hash(key, self.capacity, i**2)]
                # if element already exists, replace value and break
                if x.key == key:
                    x.value = value
                    return
                i += 1
            # at this point, we can insert in a bucket
            self.hash[q_hash(key, self.capacity, i**2)] = Node(key, value)
            self.size += 1
            self.check_load_factor()

    def get(self, key: int) -> int:
        index_to_check = primary_hash(key, self.capacity)
        if self.hash[index_to_check] == None:
            return -1
        if self.hash[index_to_check].key == key:
            return self.hash[index_to_check].value
        else:
            i = 1
            while self.hash[q_hash(key, self.capacity, i**2)] != None:
                # if element already exists, replace value and break
                x = self.hash[q_hash(key, self.capacity, i**2)]
                if x.key == key:
                    return x.value
                i += 1
            # at this point, we know that it doesn't exist.
            return -1

    def remove(self, key: int) -> bool:
        index_to_check = primary_hash(key, self.capacity)           
        if self.hash[index_to_check] != None and self.hash[index_to_check].key == key:
            self.hash[index_to_check] = None
            self.size-=1
            return True
        else:
            i = 1
            while self.hash[q_hash(key, self.capacity, i**2)] != None:
                # if element already exists, replace value and break
                x = self.hash[q_hash(key, self.capacity, i**2)]
                if x.key == key:
                    self.hash[q_hash(key, self.capacity, i**2)] = None
                    self.size-=1
                    return True
                i += 1
            return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_hash = HashTable(new_capacity)

        for node in self.hash:
            if node == None:
                continue
            else:
                new_hash.insert(node.key, node.value)
        self.hash = new_hash.hash
        self.capacity = new_capacity

    def check_load_factor(self):
        load_factor = self.getSize() / self.capacity
        if load_factor >= 0.5:
            self.resize()
