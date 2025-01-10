class dict:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def put(self,key,value):
        hash_value=self.hash_func(key)
        if self.slots[hash_value]==None:
            self.slots[hash_value]=key
            self.data[hash_value]=value
        if self.slots[hash_value]==key:
            self.data[hash_value]=value
        else:
            newhash=self.rehash(hash_value)

            while not self.slots[newhash]==None and self.slots[newhash]!=key:
                newhash=self.rehash(newhash)
            if self.slots[newhash]==None:
                self.slots[newhash]=key
                self.data[newhash]=value
            elif self.slots[newhash]==key:
                self.data[newhash]=value
            else:
                self.size*=2
                self.put(key,value)
    def hash_func(self,key):
        return abs(hash(key))%self.size
    def rehash(self,old_hash):
        return (old_hash+1)%self.size
    def get(self,key):
        start=self.hash_func(key)
        curr=start
        if self.slots[start]==key:
            return self.data[start]

        while self.slots[curr] is not None:
            curr=self.rehash(curr)
            if self.slots[curr]==key:
                return self.data[curr]
            if curr==start:
                return "NOt FOUND (list is full)"
        return "NOT FOUND(none is found) "
    def __getitem__(self, item):
        return self.get(item)
d1=dict(5)
d1.put(5,3)
d1.put(10,11)
d1.put(15,11)
d1.put(12,11)
print(d1.slots)
print(d1[182])
