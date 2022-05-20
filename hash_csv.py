import csv

class hashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        with open('nyc_weather.csv') as file:
            self.content = file.readlines()

    def get_hash(self, key):

        num = 0
        for i in key:
            num += ord(i)
        return num % self.MAX

    def __setitem__(self, key, value):

        found = False
        h = self.get_hash(key)
        for index, item in enumerate(self.arr[h]):
            if len(item) == 2 and item[0] == key:
                self.arr[h][index] == (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def pop_table(self):

        convertion_list = []
        for (i) in range(1, self.MAX +1):
            x = self.content[i].split(',')
            convertion_list.append(x)
            for i in convertion_list:
                self.__setitem__(i[0], i[1])







a = hashTable()
a.pop_table()
print(a.arr)
