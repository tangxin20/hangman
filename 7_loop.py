#name = "Ted."
#for e in name:
#    print(e)

#shows = ["GOT", "Narcos", "Vice"]
#for show in shows:
#    print(show)

#coms = ("A.Develepment", "Friends", "Always Sunny")
#for show in coms:
#    print(show)

#people = {"G.Bluth II": "A.Development", "Barney": "HIMYM", "Dennis": "Always Sunny"}
#for c in people:
#    print(c)

#tv = ["GOT", "Narcos", "Vice"]
#i = 0
#for show in tv:
#    tv[i] = tv[i].upper()
#    i += 1
#print(tv)

#tv = ["GOT", "Narcos", "Vice"]
#coms = ["Arrested Development", "friends", "Always Sunny"]
#all_shows = []
#for show in tv:
#    show = show.upper()
#    all_shows.append(show)
#for show in coms:
#    show = show.upper()
#    all_shows.append(show)
#print(all_shows)

#a = "abcdefghic"
#b = len(a)
#for i in range(0, b):
#    if "c" == a[i]:
#        print(i)

# a = "abcdefghic"
# b = len(a)
# i = 0
# while i < b:
#     if "c" == a[i]:
#         print(i)
#     i += 1

#x = 10
#while x > 0:
#    print("{}".format(x))
#    x -= 1
#print("Happy New year!")

#while 1:
#    print("Hello world!")
#    break

#qs = ["What you name?",
#      "Do you have syster?",
#      "Do you have brother?"]
#n = 0
#while True:
#    print("Type q to quit.")
#    a = input(qs[n])
#    if a == "q":
#        break
#    n = (n+1)%3

#for i in range(1, 6):
#    while i not in (1, 3):
#        print(i)
#        break

#for i in range(1, 6):
#    if i in (2, 3):
#        continue
#    print(i)


#i = 1
#while i <= 5:
#    if i == 3:
#        i += 1
#        continue
#    print(i)
#    i += 1

#for i in range(1, 3):
#    print(i)
#    for d in ("a", "b"):
#        print(d)
#        for a in ("!", "@"):
#            print(a)

#for i in range(1, 3):
#    print(i)
#    c = "ab"
#    d = 0
#    while d < len(c):
#        print(c[d])
#        d += 1

#for i in range(1, 3):
#    print(i)
#    c = "ab"
#    a = 0
#    while a in range(0, len(c)):
#        print(c[a])
#        a += 1

#i = 0
#f = "12"
#while i in range(0, len(f)):
#    print(f[i])
#    a = "ab"
#    for c in range(0, len(a)):
#        print(a[c])
#    i += 1

#while input('y or n?') != 'n':
#    for i in range(1,3):
#        print(i)
#    break

#a = ["The Walking Dead", "Entourage", "The Soparanos", "The vampire Diaries"]
#for i in a:
#    b = i
#    for c in b:
#        if c != " ":
#            print(c)

#for i in range(26, 50):
#    print(i)

#a = ["The Walking Dead", "Entourage", "The Soparanos", "The vampire Diaries"]
#b = 0
#for i in a:
#    for c in i:
#        print(str(b)+" "+c)
#        b += 1
#while True:
#    try:
#        number = (2, 6, 8)
#        answer = input("Guess a number or type q to quit: ")
#        if answer == "q":
#            break
#        elif int(answer) in number:
#            print("Right! ")
#        else:
#            print("Wrong!")
#    except(ValueError):
#        print("Please type a number!")

#List1 = [8, 19, 148, 4]
#List2 = [9, 1, 33, 83]
#List3 = []
#for i in List1:
#    for m in List2:
#        List3.append(i*m)
#print(List3)
