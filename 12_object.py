#def compare(first, second):
#    if first is second:
#        print("True")
#    else:
#        print("False")
#
#
#compare("I am tangxin 1983", "I am tangxin 1983")

#class Square():
#    s = ""
#    def __init__(self, l):
#        self.len = l
#        print("""{} by {} by {} by {}""".format(self.len, self.len, self.len, self.len))
#
#
#Square(29)

#class Square():
#    square_list = []
#    def __init__(self, w, l):
#        self.width = w
#        self.len = l
#        self.square_list.append([self.width, self.len])
#
#
#s1 = Square(2, 3)
#s2 = Square(4, 5)
#print(Square.square_list)


#x = None
#if x is None:
#    print("x is None :(")
#else:
#    print("x is not None")




#class Person():
#    def __init__(self):
#        self.name = "Tangxin"
#
#n = Person()
#sn = n
#print(sn is n)
#
#n2 = Person()
#print(n2 is nmmm)



#class AlwaysPositive:
#    def __init__(self, number):
#        self.n = number
#
#    def __add__(self, other):
#        return abs(self.n + other.n)
#
#
#x = AlwaysPositive(-20)
#y = AlwaysPositive(8)
#z = AlwaysPositive(5)
#print(x.__add__(y))
#print(x + z)



#class Lion:
#    def __init__(self, name):
#        self.name = name
#
#    def __repr__(self):
#        return self.name
#
#
#L = Lion("Dilbert")
#print(L)





#class Rectangle():
#    recs = {}
#    def __init__(self, w, l):
#        self.width = w
#        self.len = l
#        self.recs[self.width] = self.len
#
#
#r1 = Rectangle(10, 24)
#r2 = Rectangle(20, 40)
#r3 = Rectangle(100, 200)
#print(Rectangle.recs)






#class Horse():
#    def __init__(self, c, w, a, r):
#        self.color = c
#        self.weight = w
#        self.age = a
#        self.rider = r
#
#class Rider():
#    def __init__(self, n, s, a):
#        self.name = n
#        self.sex = s
#        self.age = a
#
#
#r1 = Rider("Tangxin", "man", "36")
#h1 = Horse("Red", "150kg", 5, r1)
#print(h1.rider.name)





#class Shape():
#    def __init__(self, w, l=0):
#        self.width = w
#        self.len = l
#
#    def what_am_i(self):
#        print("I am a Shape")
#
#
#class Rectangle(Shape):
#    def zhouchang(self):
#        return (self.width + self.len) * 2
#
#    def what_am_i(self):
#        print("I am a Rectangle")
#
#
#class Square(Shape):
#    def zhouchang(self):
#        return self.len * 4
#
#
#r1 = Rectangle(5, 4)
#r1.what_am_i()
#print(r1.zhouchang())
#
#s1 = Square(2, 6)
#s1.what_am_i()
#print(s1.zhouchang())








#class Shape():
#    def __init__(self):
#        self.m = "I am a shape"
#
#    def what_am_i(self):
#        print(self.m)
#
#
#class Rectangle(Shape):
#    def zhouchang(self, w, l):
#        self.width = w
#        self.len = l
#        return (self.width + self.len) * 2
#
#    def what_am_i(self):
#        print("I am a Rectangle")
#
#
#class Square(Shape):
#    def zhouchang(self, l):
#        self.len = l
#        return self.len * 4
#
#
#r1 = Rectangle()
#r1.what_am_i()
#print(r1.zhouchang(2, 3))
#
#s1 = Square()
#s1.what_am_i()
#print(s1.zhouchang(2))

#class Rectangle():
#    def __init__(self, w, l):
#        self.width = w
#        self.len = l
#
#    def zhouchang(self):
#        return (self.width + self.len) * 2
#
#
#class Square():
#    def __init__(self, l):
#        self.len = l
#
#    def zhouchang(self):
#        return self.len * 4
#
#
#rec = Rectangle(2, 9)
#print(rec.zhouchang())
#sq = Square(7)
#print(sq.zhouchang())



#class Dog:
#    def __init__(self, name, breed, owner):
#        self.name = name
#        self.breed = breed
#        self.owner = owner
#
#
#class Person:
#    def __init__(self, name):
#        self.name = name
#
#
#mick = Person("Mick Jagger")
#stan = Dog("Stanley", "Bulldog", mick)
#print(stan.owner.name)

#class Shape():
#    def __init__(self, w, l):
#        self.width = w
#        self.len = l
#
#    def print_size(self):
#        print("""{} by {}
#        """.format(self.width, self.len))
#
#class Square(Shape):
#    def area(self, s, p):
#        self.size = s
#        self.price = p
#        return self.width * self.len + self.size + self.price
#
#    def print_size(self):
#        print("""I am {} by {}
#        """.format(self.width, self.len))
#
#
#a_square = Square(20, 20)
#a_square.print_size()
#print(Square.area(6, 3))

#class Data:
#    def __init__(self):
#        self.nums = [1, 2, 3, 4, 5]
#
#    def change_data(self, index, n):
#        self.nums[index] = n
#
#
#data_one = Data()
#data_one.nums[0] = 100
#print(data_one.nums)
#
#data_two = Data()
#data_two.change_data(0, 100)
#print(data_two.nums)

#class Sjx:
#    def __init__(self, l, h):
#        self.len = l
#        self.hight = h
#
#    def area(self):
#        return self.len * self.hight * 0.5
#
#
#a = Sjx(2, 6)
#print(a.area())



#class Apple():
#    def __init__(self, w, c, s, p):
#        self.weight = w
#        self.color = c
#        self.size = s
#        self.price = p
#        print("Created!")
#
#
#ap1 = Apple(1, "red", "big", 4.5)
#print(ap1.color)

#class Rectangle():
#    def __init__(self, w, l):
#        self.width = w
#        self.len = l
#
#    def area(self):
#        return self.width * self.len
#
#    def change(self, w, l):
#        self.width = w
#        self.len = l
#
#
#rec = Rectangle(10, 20)
#print(rec.area())
#rec.change(20, 40)
#print(rec.area())



#class Orange:
#    def __init__(self, w, c):
#        """重量的单位是盎司"""
#        self.weight = w
#        self.color = c
#        self.mold = 0
#        print("Created!")
#
#    def rot(self, days, temp):
#        self.mold = days*temp
#
#
#orange = Orange(6, "dark orange")
#print(orange.mold)
#orange.rot(20, 40)
#print(orange.mold)

#class Orange:
#    def __init__(self, w, c):
#        self.weight = w
#        self.color = c
#        print("Created!")
#or1 = Orange(1, "dark orange")
#or1.weight = 100
#or1.color = "light orange"
#print(or1.weight)
#print(or1.color)