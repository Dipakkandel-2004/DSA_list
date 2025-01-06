class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.n=0
    def enqueue(self,item):
        if self.rear==None:
            new_node=node(item)
            self.front=new_node
            self.rear = self.front
        else:
            new_node=node(item)
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front==None:
            print("Queue is empty")
            return
        else:
            self.front= self.front.next
    def __str__(self):
        temp=self.front
        result=""
        while temp is not None:
            result=result+str(temp.data)+"<--"
            temp=temp.next
        return result[:-3]
q1=queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
q1.dequeue()
print(q1)
