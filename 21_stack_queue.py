class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


a = [1, 2, 3, 4, 5]
b = Stack()
c = []
for i in a:
    b.push(i)
for i in range(len(b.items)):
    c.append(b.pop())
print(c)





#class Stack:
#    def __init__(self):
#        self.items = []
#
#    def is_empty(self):
#        return self.items == []
#
#    def push(self, item):
#        self.items.append(item)
#
#    def pop(self):
#        return self.items.pop()
#
#    def peek(self):
#        last = len(self.items)-1
#        return self.items[last]
#
#    def size(self):
#        return len(self.items)
#
#
#a = "yesterday"
#b = Stack()
#c = ""
#for i in a:
#    b.push(i)
#for i in range(len(b.items)):
#    c += b.pop()
#print(c)


#import time
#import random
#
#
#class Queue:
#    def __init__(self):
#        self.items = []
#
#    def is_empty(self):
#        return self.items == []
#
#    def enqueue(self, item):
#        self.items.insert(0, item)
#
#    def dequeue(self):
#        return self.items.pop()
#
#    def size(self):
#        return len(self.items)
#
#    def simulate_line(self, till_show, max_time):
#        pq = Queue()
#        tix_sold = []
#        for i in range(100):
#            pq.enqueue("person" + str(i))
#        t_end = time.time() + till_show
#        now = time.time()
#        while now < t_end and not pq.is_empty():
#            now = time.time()
#            r = random.randint(0, max_time)
#            time.sleep(r)
#            person = pq.dequeue()
#            print(person)
#            tix_sold.append(person)
#        return tix_sold
#
#
#queue = Queue()
#sold = queue.simulate_line(5, 2)
#print(sold)

#class Queue:
#    def __init__(self):
#        self.items = []
#
#    def is_empty(self):
#        return self.items == []
#
#    def enqueue(self, item):
#        self.items.insert(0, item)
#
#
#    def dequeue(self):
#        return self.items.pop()
#
#    def size(self):
#        return len(self.items)
#
#
#a_queue = Queue()
#b = "abcd"
#c = []
#for word in b:
#    a_queue.enqueue(word)
#print(a_queue.is_empty())
#for i in range(a_queue.size()):
#    c.append(a_queue.dequeue())
#print(c)
#print(a_queue.is_empty())



#class Stack:
#    def __init__(self):
#        self.items = []
#
#    def is_empty(self):
#        return self.items == []
#
#    def push(self, item):
#        self.items.append(item)
#
#    def pop(self):
#        return self.items.pop()
#
#    def peek(self):
#        last = len(self.items)-1
#        return self.items[last]
#
#    def size(self):
#        return len(self.items)


#stack = Stack()
#for c in "TangXin":
#    stack.push(c)
#reverse = ""
#for i in range(len(stack.items)):
#    reverse += stack.pop()
#
#print(reverse)
