#a = "Hello".upper()
#b = "Hellooo".replace("o", "@")
#print(a,b)

#fruit = list("a", "b", "c")
#f2 = []
#f2.append("g")
#f2.append("h")
#f2.append(100)
#f2.append(1.2)
#f2.append(True)
#f2.append(False)
#f2[2] = "60"
#print(f2)
#print(f2[2])

#colors = ["blue", "green", "yellow"]
#print(colors)
#item = colors.pop()
#print(item)
#print(colors)
#item = colors.pop()
#print(item)
#print(colors)
#item = colors.pop()
#print(item)
#print(colors)

#colors = [1]
#print(colors.pop())
#print(colors)
#L1 = [1]
#L2 = [2]
#L3 = [3]
#L4 = L1 + L2 + L3
#print(len(L4))
#print(2 not in L1)

#colors = ["purple", "orange", "green"]
#guess = input("Guess a color: ")
#if guess in colors:
#    print("You guess correctly!")
#else:
#    print("Wrong! try again.")

#my_tuple = ("c",)
#my_tuple = ("d", "e")
#print(my_tuple[1])
#print( "i" not in my_tuple)

#print(dict())
#print({})
#fruits = {"Apple": "Red", "Banana": "Yellow"}
#print(fruits)
#facts = dict()
#facts = {1: "Red", 2: "Yellow"}
#facts[3]="fun"
#facts[3]="black"
#print(facts)
#print(facts[1])
#print(4 not in facts)
#print(facts)

#books = {"Dracula": "Stoker", "1984": "Orwell", 3: "Kafka"}
#books[4] = "aaaa"
#del books[4]
#print(books)

#word = {"the": "fox", "jumped": "up"}
#one = " ".join(word)
#print(word["the"])
#word = {"a":"the", "b":"fox", "tang":"jump"}
#two = word["a"]
#print(two)

#a = "abc"
#b = "*".join(a)
#print(b)

#a = "     The bird    "
#b = a.strip()
#print(b)

#a = "The bird is 50$,and The dog is 500$"
#b = a.replace("$", "元")
#print(b)

#a = "abcdefg"
#b = a.index("b")
#print(b)

#try:
#    a = "abcd"
#    b = a.index("c")
#    print(b)
#except:
#    print("Not Found!")

#a = "e"
#b = "bdeat"
#c = a in b
#print(c)

#a = "abcd"
#print(a[2:4])
#a = ["a", "b", "c", "d"]
#print(a[2:4])

#print("she said 'Surely'")
#print('She said "Surely"')
#print("She said \"Surely\"")

#a = input("input the first string:")
#b = input("input the second string:")
#c ="Yesterday I wrote a {}. I sent it to {}!".format(a, b)
#print(c)

#print("a\nb\nc\nd\ne")

#a = "zhangsan tangxin."
#b = a[0:1].upper() + a[1:]
#print(b)

#a = "Where now? Who now? When now?"
#b = a.split("?")
#i = 0
#e = []
#while b[i] != '':
#    f = "{}?".format(b[i])
#    e.append(f)
#    i += 1
#print(e)

a = "Where now? Who now? When now?"
b = len(a)
c = a.index("?")
i = 0
d = []
d.append(a[:c+1])
#try:
#    while i <= b:
#        e = c
#        c = a.index("?", c+1, b)
#        print(c)
#        f = (a[e+1:c+1]).strip()
#        print(f)
#        d.append(f)
#        i = c
#except(ValueError):
#    print("Search complet!")
#print(d)


#a = ("The", "fox", "jumped", "over", "the", "fence", ".")
#b = " ".join(a)
#c = b.replace(" .", ".")
##d = c.strip()
##e = "{}.".format(d)
#print(c)

#a = "A screaming comes across the sky."
#b = a.replace("s", "$")
#print(b)

#a = "aymasdm3asdaadfmaa"
#b = len(a)
#c = a.index("ma")
#i = 0
#try:
#    while i <= b:
#        print(c)
#        c = a.index("ma", c+1, b)
#        i = c
#except(ValueError):
#    print("Search complet!")

#a = "three"
#b = (a+" ")*3
#b = b.strip()
#print(b)
#c = "{} {} {}".format(a, a, a)
#print(c)
#d = []
#i = 0
#while i < 3:
#    d.append(a)
#    i += 1
#e = " ".join(d)
#print(e)
#a ="three"
#b = a+" "+a+" "+a
#print(b)

#a = "abcdefghic"
#b = len(a)
#i = 0
#for i in range(0, b):
#    if "c" == a[i]:
#        print(i)
#    i += 1
#
#a = "abcdefghic"
#b = len(a)
#i = 0
#while i < b:
#    if "c" == a[i]:
#        print(i)
#    i += 1

#a = "It was bright cold day in April,and the clocks were striking thirteen."
#print(a.split(",")[0])
