import csv
class hashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        with open('nyc_weather.csv') as file:
            self.content = file.readlines()
        print(self.content)

    def get_hash(self, key):

        num = 0
        for i in key:
            num += ord(i)
        print(self.arr)
        return num % self.MAX

    def pop_table(self):
        convertion_list = []
        for (i) in range(1, self.MAX +1):
            x = self.content[i].split(',')
            convertion_list.append(x)
            print(self.content[i])
            print(convertion_list)





a = hashTable()
b = a.get_hash('narch 6546546754')
a.pop_table()
print(b)