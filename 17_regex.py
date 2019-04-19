#import re
#m = "The ghost that says boo huants the loo."
#b = re.findall(".oo", m)
#print(b)

#import re
#m = "Arizona 479、501、870. Carlifornia 209、213、650。"
#b = re.findall("\\d", m)
#print(b)


#import re
#word = """I love the flower,
#and my wife love the water.
#Do you love me?"""
#m = re.findall("love.*?", word, re.MULTILINE)
#print(m)

#import re
#line = "I love $"
#m = re.findall("\\$", line, re.IGNORECASE)
#print(m)


#import re
#text = """
#The first name is __name__.
# The second name is __name__.
# The three name is __name__.
# The four name is __name__."""
#
#
#def mad_libs(mls):
#    hints = re.findall("__.*?__", mls)
#    if hints is not None:
#        for word in hints:
#            q = "Enter a {}".format(word)
#            new = input(q)
#            mls = mls.replace(word, new)
#            print("\n")
##             mls = mls.replace("\n", "")
#    else:
#        print("invalid mls")
#    print(mls)
#
#
#mad_libs(text)

#import re
#f = "__one__tow__three__four__five__"
#found = re.findall("__.*?__", f)
#for match in found:
#    print(match)

#import re
#line = "12_3?459dhello0?"
#m = re.findall("\\d", line, re.IGNORECASE)
#print(m)

#import re
#st = "Two too"
#m = re.findall("t[wo]o", st, re.IGNORECASE)
#print(m)


#import re
#zen = """Although never is
#often better than
#*right* now.
#If the implementation is hard to explain.
#If you are right.
#You are right.
#You are beautiful."""
#m = re.findall("^Y", zen, re.MULTILINE)
#print(m)
 


#import re
#a = "Beautiful is better than ugly."
#matches = re.findall("beautiful", a, re.IGNORECASE)
#print(matches)
