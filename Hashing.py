def Hash_val(val):
    a=0
    for i in val:
        a+=ord(i)
    return a % 100
print(Hash_val("march 6"))
class hastable:
    def __init__(self):
        self.max=10
        self.list=[None for i in range(self.max)]

    def Hash_val( self,val):
        a = 0
        for i in val:
            a += ord(i)
        print(a)
        return a % self.max
    def add(self,key,value):
        a = self.Hash_val(key)
        self.list[a]=value
h1=hastable()
h1.add("DIPAdseewFeeK","33")
h1.add("DIPeaseAK","33")
h1.add("DIP2 AWEFeK","33")
h1.add("DIPAKwweddf","33")
print(h1.list)
