
class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class linklist:
    def __init__(self):
        self.n = 0
        self.head = None

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            print(str(curr.key) + "-->" + str(curr.value), end=" ")
            curr = curr.next
        return ""

    def insert_at_tail(self, key, item):
        newnode = node(key, item)
        if self.head == None:
            self.head = newnode
            self.n+=1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newnode
            self.n += 1

    def delete_by_value(self, key):
        curr = self.head
        if self.head == None:
            return
        if self.head.key == key:
            self.head = self.head.next
            self.n -= 1
            return
        else:
            while curr.next is not key:
                if curr.next.key == key:
                    print("value not found")
                    break
                curr= curr.next
                if curr.next==None:
                    return "NOTFOUND"
                else:
                    curr.next=curr.next.next


    def search_by_value(self, key):
        idx = 0
        curr = self.head
        flag = False
        while curr != None:
            if curr.key == key:
                flag = True
                return idx
            curr = curr.next
            idx += 1
        if flag == False:
            return -1

    def search_by_index(self, idx):
        curr = self.head
        counter=0
        while curr is not None:
            if counter==idx:
                return curr
            curr=curr.next
            counter+=1


class dict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(linklist())
        return L

    def put(self, key, value):
        bucket_index = self.hash_func(key)
        node_idx = self.get_node_idx(bucket_index, key)
        if node_idx == -1:
            self.buckets[bucket_index].insert_at_tail(key, value)
            self.size += 1
            load_factor = self.size / self.capacity
            if load_factor>=2:
                self.rehash()

        else:
            curr = self.buckets[bucket_index].search_by_index(node_idx)
            curr.value = value
    def rehash(self):
        self.capacity=self.capacity*2
        old_bucket=self.buckets
        self.size=0
        self.buckets=self.make_array(self.capacity)
        for i in old_bucket:
            for j in range(i.n):
                new_node=i.search_by_index(j)
                key=new_node.key
                val=new_node.value
                self.put(key,val)



    def get_node_idx(self, bucket_index, key):
        node_idx = self.buckets[bucket_index].search_by_value(key)
        return node_idx

    def hash_func(self, key):
        return abs(self.cal_hash(key)) % self.capacity

    def __setitem__(self, key, value):
        self.put(key,value)
    def __getitem__(self, key):
        return self.get(key)
    def get(self,key):
        bucket_index = self.hash_func(key)
        res=self.buckets[bucket_index].search_by_value(key)
        if res==-1:
            return "NOT FOUND"
        else:
            node=self.buckets[bucket_index].search_by_index(res)
            return node.value
    def cal_hash(self,key):
        result = 0
        for char in str(key):
            result = result * 31 + ord(char)
        return result
    def __delitem__(self, key):
        return self.Delete(key)
    def Delete(self,key):
        bucket_index = self.hash_func(key)
        self.buckets[bucket_index].delete_by_value(key)
        self.size-=1



d1 = dict(1)
d1.put("c_sharp",100)
d1.put("cpp",100)
d1.put("java",100)
d1.put("javascript",100)
d1["ruby"]= 450
d1.__delitem__("cpp")
print(d1.get("ruby"))
print( d1.buckets[0].__str__())
print( d1.buckets[1].__str__())
print( d1.buckets[2].__str__())
print( d1.buckets[3].__str__())

