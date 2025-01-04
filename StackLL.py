class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        self.n=0
    def isempty(self):
        return self.top == None
    def __len__(self):
        return self.n
    def push(self,value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node
        self.n+=1
    def pop(self):
        temp=self.top
        if self.isempty() is False:
            self.top=self.top.next
            self.n-=1

    def __str__(self):
        temp=self.top
        result=""
        while temp is not None:
            result=result+"["+str(temp.data)+"]"+"\n"
            temp=temp.next
        return result

s1=stack()
print(s1.isempty())
s1.push(90)
s1.push(20)
s1.push(70)
s1.push(45)
s1.pop()
s1.pop()
print(s1)
print("The size of stack is ",len(s1))
print(s1.isempty())
