import sys
import re
from collections import deque

filename = sys.argv[1]

file = open(filename, "r")

contents = file.read()

class Char:
    def __init__ (self, intvalue): 
        self.char = chr(intvalue)
    def asString(self):
        return self.char
    def change(self, intvalue):
        self.char = chr(intvalue)
    def change(self, strvalue):
        if (len(strvalue)!=1):
            return
        else:
            self.char = strvalue

def char(s):
    ch = Char(0)
    ch.change(s)
    return ch

q = deque()
vars = {}
types = {'i': int, 's': str, 'c': char}


pointer = -1

i = 0
while (i<len(contents)):
    print(q)
    print(vars)
    if (contents[i]=="@"):
        while (contents[i]!="%"):
            i+=1
    elif (contents[i]=="\""):
        j = i
        while (contents[j]!="\'"):
            j+=1
        q.appendleft(contents[i+1:j])
        i=j
    elif (contents[i]=="|"):
        i+=1
        val = q.popleft()
        bval = False
        try:
            val = types[contents[i]](val)
        except:
            pass
        i+=1
        j = i
        while (contents[j]!=":"):
            j+=1
        vars[contents[i+1:j]]=val
        i=j
    elif (contents[i]=="^"):
        if (q[0] in vars): q.appendleft(vars[q.popleft()])
    elif (contents[i]==":"):
        if (q[0] in vars): vars[q.popleft()]=q.popleft()
    elif (contents[i]=="!"):
        del q[0]
    elif (contents[i]=="?"):
        q.clear()
    elif (contents[i]=="~"):
        val = q.popleft()
        if (val < 0):
            q.appendleft(-1)
        elif (val > 0):
            q.appendleft(1)
        else:
            q.appendleft(0)
    elif (contents[i]=="]"):
        q.appendleft(None)
    elif (contents[i]=="["):
        q.appendleft(q.popleft()[int(q.popleft())])
    elif (contents[i]==";"):
        print(q[0])
    elif (contents[i]=="&"):
        q.appendleft(q[0])
    elif (contents[i]=='+'):
        q.appendleft(int(q.popleft())+int(q.popleft()))
    elif (contents[i]=='-'):
        q.appendleft(int(q.popleft())-int(q.popleft()))
    elif (contents[i]=='/'):
        q.appendleft(int(q.popleft())//int(q.popleft()))
    elif (contents[i]=='*'):
        q.appendleft(int(q.popleft())*int(q.popleft()))
    else:
        try: q.appendleft(int(contents[i]))
        except: pass
    i+=1

# print (contents)

print ()
print ()
print(q)
print(vars)
input("End of Program, Press Return to Exit (Consumes CPU if you Don't) ")