class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        self.n=0
    def __len__(self):
        return self.n

    def push(self,item):
        newnode=node(item)
        newnode.next=self.top
        self.top=newnode
        self.n+=1
    def pop(self):
        if self.isempty():
            return
        else:
            data=self.top.data
            self.top= self.top.next
            self.n-=1
            return data
    def __str__(self):
        temp=self.top
        result=""
        while temp is not None:
            result=result+str(temp.data)
            temp=temp.next
        return result
list=[
    [0,0,1,1],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,1,0]
]

def find_celebrity(List):
    s1 = stack()
    for i in range(len(list)):
        s1.push(i)
    while len(s1)>=2:
        i=s1.pop()
        j=s1.pop()
        if List[i][j]==0:
            s1.push(i)
        else:
            s1.push(j)
    celeb=s1.pop()
    result=False
    for i in range(len(list)):
        if i!=celeb:
            if list[i][celeb]==0 or list[celeb][i]==1:
                print("NO one is celebrity")
                return
    print("Celebrity is ",celeb)

find_celebrity(list)
