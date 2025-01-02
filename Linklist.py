class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linklist:
    def __init__(self):
        self.n=0
        self.head=None
    def __len__(self):
        return self.n
    def insert_at_head(self,item):
        newnode=node(item)
        newnode.next=self.head
        self.head=newnode
        self.n+=1
    def __str__(self):
        curr=self.head
        result=""
        while curr !=None:
            result=result+str(curr.data)+"-->"
            curr=curr.next
        return result[:-3]
    def insert_at_tail(self,item):
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        newnode=node(item)
        newnode.next=None
        curr.next=newnode
        self.n+=1
    def insert_at_given_pos(self,item,pos):
        curr=self.head
        count=1
        if pos>self.n:
            print("Index doesnt exist")
            return
        while count!=pos-1:
            curr=curr.next
            count+=1
        newnode=node(item)
        newnode.next=curr.next
        curr.next=newnode
        self.n+=1
    def insert_after_given_value(self,value,item):

        curr=self.head
        while curr.data!=value:
            if curr.next==None and curr.data!=value:
                # print("Value not founddd")
                return
            curr=curr.next
        newnode=node(item)
        newnode.next=curr.next
        curr.next=newnode
        self.n+=1
    def clear(self):
        self.head=None
        self.n=0
    def delete_from_head(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.n-=1

    def delet_from_tail(self):
        curr=self.head
        if self.head==None:
            return
        if self.head.next==None:
            self.head=None
            self.n-=1
            return
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n-=1
    def delete_by_value(self,value):
        curr=self.head
        if self.head==None:
            return
        if self.head.data==value:
            self.head=self.head.next
            self.n-=1
            return
        while curr.next.data is not value and curr.next is not None:
            curr=curr.next
            if curr.next==None:
                print("value not found")
                return
        curr.next=curr.next.next
        self.n-=1
    def search_by_value(self,value):
        idx=1
        curr=self.head
        flag=False
        while curr.next!=None:
            if curr.data==value:
                print("Element found in index- ",idx)
                flag=True
            curr=curr.next
            idx+=1
        if flag==False:
            print("Not foundd")
    def search_by_index(self,idx):
        curr=self.head
        for i in range(1,self.n+1):
            if i==idx:
                print(curr.data)
                return
            curr=curr.next

    def delete_by_index(self,idx):
        if idx<1 or idx>self.n:
            print("index error")
            return
        count=1
        curr=self.head

        while idx-1!=count:
            if idx == 1:
                self.head = self.head.next
                self.n -= 1
                return
            curr=curr.next
            count+=1
        curr.next=curr.next.next
        self.n-=1
l1=linklist()
l1.insert_at_head(20)
l1.insert_at_head(22)
l1.insert_at_head(224)
l1.insert_at_head(2244)
l1.insert_at_head(4422)
l1.insert_at_tail(922)
l1.insert_at_tail(2252)
l1.insert_at_tail(487)
l1.insert_at_given_pos(2025,3)
l1.insert_after_given_value(22,50505)
l1.delete_from_head()
l1.delete_from_head()
l1.delete_by_value(22222)
l1.delete_by_value(50505)
l1.search_by_value(22)
l1.search_by_value(202)
l1.delete_by_index(1)
print(len(l1))
print(l1)
