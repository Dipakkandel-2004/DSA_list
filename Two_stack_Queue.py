class node:
    def __init__(self, value):
        self.data = value
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top == None

    def __len__(self):
        return self.n

    def push(self, value):
        new_node = node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    def pop(self):
        if self.isempty():
            return
        else:
            data=self.top.data
            self.top= self.top.next
            self.n-=1
            return data

    def __str__(self):
        temp = self.top
        result = ""
        while temp is not None:
            result = result +str(temp.data) + ","
            temp = temp.next
        return result

    def peak(self):
        if self.isempty():
            return "Stack is empty"
        else:
            print(self.top.data)

    def rev(self):
        temp = self.top
        result = ""
        while temp != None:
            result =str(temp.data)+","+ result
            temp = temp.next
        return result[:-1]


s1 = stack()
s2 = stack()
def enqueue(item):
    s1.push(item)


def dequeue():
    if s2.isempty():
        while not s1.isempty():
            s2.push(s1.pop())
    if s2.isempty():
        print("queue is empty")
        return None
    else:
     return s2.pop()
def show_queue():
    temp_stack = stack()
    temp = s2.top
    while temp is not None:
        temp_stack.push(temp.data)
        temp = temp.next
    temp = s1.top
    while temp is not None:
        temp_stack.push(temp.data)
        temp = temp.next
    result = ""
    while not temp_stack.isempty():
        result += str(temp_stack.pop()) + " "

    print("Remaining elements in queue:", result.strip())

enqueue(21)
enqueue(22)
enqueue(23)
show_queue()
dequeue()
enqueue(2)
enqueue(3)
enqueue(3)
dequeue()
show_queue()

