#def f(x):
#    return x**3
#a=f(int(input("Please input a number:")))
#if a < 100:
#    print("result < 100")
#if a < 50:
#    print("result < 50")
#else:
#    print("error")

#def f():
#    return 1+2
#print(f())

#def f(x,y,z):
#    return x*y*z
#a =  int(input("please input first number:") )
#b =  input("please input second number:")
#c =  input("please input third number:")
#d = f(a,b,c)
#print("The result is:"+str(d))

#def f():
#    """
#    返回n的平方的值
#    :param n:ini.
#   :return:int,n的平方
#    """
#    n = int(input("Please input a number:"))
#    return n**2
#print("您输入数字的平方值为："+str(f()))

#def f():
#    n = str(input("Please input a string:"))
#    print(n)
#f()

#def f(a,b,c,d=2,e=3):
#    """
#    返回a+b+c+d+e的值
#    :param a:int.
#    :param b:int.
#    :param c:int.
#    :param d:int.
#    :param e:int.
#    :return:int,求a,b,c,d,e之和。
#    """
#    return(a+b+c+d+e)
#print(f(10,10,10,10,10))


#def fun1():
#   """
#   将输入的数字取整数并除以2，然后将结果返回。
#   :return:int,取整并除以2
#   """
#   a = input("Please input a number:")
#   try:
#       c = int(a)/3
#       return int(c)
#   except (ValueError):
#       print("Please input a int number")
#b=fun1()
#print(b)
#def fun2():
#    """
#    调用全局参数b，然后将b乘以4的结果打印出来。
#    :return: 无返回，直接打印b*4的结果。
#    """
#    global b
#    try:
#        c = b*4
#        print("The result is: " +str(c) )
#    except (TypeError):
#        print("not number!")
#fun2()

#def to_float():
#    """
#    将字符串转换成浮点数
#    :return:没有值返回，直接打印出转换的浮点数
#    """
#    try:
#        a = input("input a number:")
#        print(float(a))
#    except (ValueError):
#        print("only for number!")
#to_float()





