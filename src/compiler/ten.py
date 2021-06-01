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

def boolexpr(s):
    if (len(s)==0):
        return True
    qc = 0
    i = 0
    while (i < len(s)):
        if (s[i]=="\""):
            j = i
            while (s[j]!="\'"):
                j+=1
            q.appendleft(s[i+1:j])
            qc+=1
            i=j
        elif (s[i]=="^"):
            if (q[0] in vars): 
                q.appendleft(vars[q.popleft()])
        elif (s[i]=="~"):
            val = q.popleft()
            if (val < 0):
                q.appendleft(-1)
            elif (val > 0):
                q.appendleft(1)
            else:
                q.appendleft(0)
        elif (s[i]=="]"):
            q.appendleft(None)
            qc+=1
        elif (s[i]=="["):
            q.appendleft(q.popleft()[int(q.popleft())])
            qc-=1
        elif (s[i]=="&"):
            q.appendleft(q[0])
            qc+=1
        elif (s[i]=='+'):
            q.appendleft(int(q.popleft())+int(q.popleft()))
            qc-=1
        elif (s[i]=='-'):
            q.appendleft(int(q.popleft())-int(q.popleft()))
            qc-=1
        elif (s[i]=='/'):
            q.appendleft(int(q.popleft())//int(q.popleft()))
            qc-=1
        elif (s[i]=='*'):
            q.appendleft(int(q.popleft())*int(q.popleft()))
            qc-=1
        elif (s[i]=='('):
            q.appendleft(q.popleft() and q.popleft())
            qc-=1
        elif (s[i]==')'):
            q.appendleft(q.popleft() or q.popleft())
            qc-=1
        elif (s[i]=='.'):
            q.appendleft(not q.popleft())
        elif (s[i]=='='):
            q.appendleft(q.popleft()==q.popleft())
            qc-=1
        elif (s[i]=='I'):
            q.appendleft(int(q.popleft()))
        elif (s[i]=='S'):
            q.appendleft(str(q.popleft()))
        elif (s[i]=='C'):
            q.appendleft(char(str(q.popleft())))
        else:
            try: q.appendleft(int(s[i]))
            except: pass
        i+=1
    ret = q.popleft()
    qc-=1
    # ideally, the below should not excecute (but it might ¯\_(ツ)_/¯)
    while (qc>0):
        q.popleft()
        qc-=1
    if (ret==True or ret==False): return ret
    else: return True
def exec(s):
    i = 0
    while (i<len(s)):
        # print(q)
        # print(vars)
        if (s[i]=="@"):
            while (s[i]!="%"):
                i+=1
        elif (s[i]=="\""):
            j = i
            while (s[j]!="\'"):
                j+=1
            q.appendleft(s[i+1:j])
            i=j
        elif (contents[i]=="|"):
            i+=1
            val = q.popleft()
            # bval = False
            try:
                val = types[s[i]](val)
            except:
                pass
            i+=1
            j = i
            while (s[j]!=":"):
                j+=1
            vars[s[i+1:j]]=val
            i=j
        elif (s[i]=="^"):
            if (q[0] in vars): q.appendleft(vars[q.popleft()])
        elif (s[i]==":"):
            if (q[0] in vars): 
                var = q.popleft()
                val = q.popleft()
                # print ((var, val))
                vars[var]=val
        elif (s[i]=="!"):
            q.popleft()
        elif (s[i]=="?"):
            q.clear()
        elif (s[i]=="~"):
            val = q.popleft()
            if (val < 0):
                q.appendleft(-1)
            elif (val > 0):
                q.appendleft(1)
            else:
                q.appendleft(0)
        elif (s[i]=="]"):
            q.appendleft(None)
        elif (s[i]=="["):
            q.appendleft(q.popleft()[int(q.popleft())])
        elif (s[i]==";"):
            print(q[0])
        elif (s[i]=="&"):
            q.appendleft(q[0])
        elif (s[i]=='+'):
            q.appendleft(int(q.popleft())+int(q.popleft()))
        elif (s[i]=='-'):
            q.appendleft(int(q.popleft())-int(q.popleft()))
        elif (s[i]=='/'):
            q.appendleft(int(q.popleft())//int(q.popleft()))
        elif (s[i]=='*'):
            q.appendleft(int(q.popleft())*int(q.popleft()))
        elif (s[i]=='('):
            q.appendleft(q.popleft() and q.popleft())
        elif (s[i]==')'):
            q.appendleft(q.popleft() or q.popleft())
        elif (s[i]=='.'):
            q.appendleft(not q.popleft())
        elif (s[i]=='='):
            q.appendleft(q.popleft()==q.popleft())
        elif (s[i]=='I'):
            q.appendleft(int(q.popleft()))
        elif (s[i]=='S'):
            q.appendleft(str(q.popleft()))
        elif (s[i]=='C'):
            q.appendleft(char(str(q.popleft())))
        elif (s[i]=='{'):
            start = ""
            j = i
            while (s[j]!=','):
                j+=1
            start = s[i+1:j]
            exec(start)
            cond = ""
            i=j
            j+=1
            while (s[j]!=','):
                j+=1
            cond = s[i+1:j]
            i=j
            j+=1
            itr = ""
            while (s[j]!=','):
                j+=1
            itr = s[i+1:j]
            body = ""
            i=j
            j+=1
            while (s[j]!='}'):
                j+=1
            body = s[i+1:j]
            i=j
            while (boolexpr(cond)):
                exec(body)
                exec(itr)
        else:
            try: q.appendleft(int(s[i]))
            except: pass
        i+=1

i = 0
while (i<len(contents)):
    # print(q)
    # print(vars)
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
        if (q[0] in vars): 
            var = q.popleft()
            val = q.popleft()
            # print ((var, val))
            vars[var]=val
    elif (contents[i]=="!"):
        q.popleft()
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
    elif (contents[i]=='('):
        q.appendleft(q.popleft() and q.popleft())
    elif (contents[i]==')'):
        q.appendleft(q.popleft() or q.popleft())
    elif (contents[i]=='.'):
        q.appendleft(not q.popleft())
    elif (contents[i]=='='):
        q.appendleft(q.popleft()==q.popleft())
    elif (contents[i]=='I'):
        q.appendleft(int(q.popleft()))
    elif (contents[i]=='S'):
        q.appendleft(str(q.popleft()))
    elif (contents[i]=='C'):
        q.appendleft(char(str(q.popleft())))
    elif (contents[i]=='{'):
        start = ""
        j = i
        while (contents[j]!=','):
            j+=1
        start = contents[i+1:j]
        # print(start)
        exec(start)
        cond = ""
        i=j
        j+=1
        while (contents[j]!=','):
            j+=1
        cond = contents[i+1:j]
        # print(cond)
        i=j
        itr = ""
        j+=1
        while (contents[j]!=','):
            j+=1
        itr = contents[i+1:j]
        # print(itr)
        body = ""
        i=j
        j+=1
        while (contents[j]!='}'):
            j+=1
        body = contents[i+1:j]
        # print(body)
        i=j
        cont = boolexpr(cond)
        # print(cont)
        while (cont):
            exec(body)
            # print("Body")
            exec(itr)
            cont = boolexpr(cond)
            # print(cont)
            # print(q)
            # print(vars)
    else:
        try: q.appendleft(int(contents[i]))
        except: pass
    i+=1

# print (contents)

print ()
print ()
# print(q)
# print(vars)
input("End of Program, Press Return to Exit (Consumes CPU if you Don't) ")