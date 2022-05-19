class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        baconhash = 0
        for lett in key:
            baconhash += ord(lett)
        return baconhash % self.max

    def __getitem__(self, index):
        baconhash = self.get_hash(index)
        return self.arr[baconhash]

    def __setitem__(self, key, val):
        found = False
        baconhash = self.get_hash(key)
        for index, item in enumerate(self.arr[baconhash]):
            if len(item) == 2  and item[0] == key:
                self.arr[baconhash][index] = (key,val)
                found = True
                break
        if not found:
            self.arr[baconhash].append((key, val))



t = HashTable()
b = t.get_hash('march 6')

t['march 14'] = 77
print(t['march 6'])