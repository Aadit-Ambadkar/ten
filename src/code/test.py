import sys
sys.setrecursionlimit(100000)
i = 0
def greet():
    global i
    i+=1
    # if (i%1000==0):
    print("Hello", i)
    greet()
greet()