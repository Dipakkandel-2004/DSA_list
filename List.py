import ctypes
class merolist:
    def __init__(self):
        self.size = 1
        self.n = 0   # It specifies number of element present in list
        self.a = self.makelist(self.size)

    def makelist(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self, item):
        if self.size == self.n:
            self.resize(self.size * 2)
        self.a[self.n] = item
        self.n = self.n + 1

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.a[i]) + ","
        return "[" + result[:-1] + "]"

    def pop(self):
        self.n = self.n - 1
        if (self.n == 0):
            return "Empty list"

    def resize(self, newcapacity):
        b = self.makelist(newcapacity)
        self.size = newcapacity
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, value):
        for i in range(self.n):
            if self.a[i] == value:
                return i

        return "Index_error"
    def insert(self,pos,item):
        if self.size == self.n:
            self.resize(self.size * 2)
        for i in (range(self.n,pos,-1)):
            self.a[i]=self.a[i-1]
        self.a[pos]=item
        self.n+=1
    def delete(self,pos):
        if 0<=pos<=self.n:
            for i in range(pos,self.n-1):
                self.a[i]=self.a[i+1]
            self.n=self.n-1
    def remove(self,item):
        pos=self.find(item)
        if 0<=pos<=self.n:
            for i in range(pos,self.n-1):
                self.a[i]=self.a[i+1]
            self.n=self.n-1
    def sort(self):
        for i in range(self.n):
            for j in range(self.n-i-1):
                if self.a[j]>self.a[j+1]:
                    self.swap(j,j+1)


    def swap(self,a, b):
            temp = self.a[a]
            self.a[a] = self.a[b]
            self.a[b] = temp
li = merolist()
li.append(22)
li.append(82)
li.append(93)
li.append(963)
li.append(903)
li.insert(1,203)
li.insert(0,69)
print(li)
li.sort()
print(li)
