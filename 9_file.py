#import os
#r = os.path.join("C:\\", "Users", "tangxin", "Desktop", "test", "file2.txt")
#print(r)

#file = open(r, "w+")
#file.write("dog")
#file.close()

#a = list()
#with open("file.txt", "r") as f:
#    a.append(f.read())
#    print(a)
#    f.write("hello tangxin")

#import csv
#with open("user_passwd.csv", "r") as f:
#    tmp = csv.reader(f, delimiter=",")
#    for row in tmp:
#        print(row)
#        print(",".join(row))

#import os
#p = os.path.join("D:\\", "zhanghao.txt")
#print(p)
#with open(p, "r", encoding="utf8") as f:
#    print(f.read())


#path = "D://zhanghao.txt"
#with open(path, "r", encoding="utf8") as f:
#    print(f.read())

#a = ("zhangsan", "lisi", "wangwu", "zhaosi")
#import csv
#with open("result.csv", "w+", encoding="utf8", newline="") as f:
#    b = csv.writer(f, delimiter=",")
#    for row in a:
#        b.writerow([row])

#a = ("zhangsan", "lisi", "wangwu", "zhaosi")
#with open("result.txt", "w", encoding="utf8") as f:
#    for row in a:
#        f.write(row)
#        f.write("\n")

a = [["唐鑫", 213127, "IT共享部"], ["程龙宝", 234123, ""]
     , ["岑荣荣", 452123, "研发部"]]
import csv
#with open("order.csv", "w", newline="", encoding="gbk") as f:
#    b = csv.writer(f, delimiter=",")
#    header = ["姓名", "工号", "部门"]
#    b.writerow(header)
#    list1 = []
#    list2 = []
#    list3 = []
#    for x in a:
#        list1 = x[0]
#        list2 = x[1]
#        list3 = x[2]
#        b.writerows(zip([list1], [list2], [list3]))

#with open("order.csv", "r", encoding="gbk") as f:
#    print(f.read())

import csv
with open("order.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(row)
        print(",".join(row))
