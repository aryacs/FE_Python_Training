'''
def dem():
    print('Welcome to recursive function')
    dem()
dem()
'''

'''
i = 0
def demo():
    global i
    i += 1
    print("Hello...", i)
    demo()

demo()
'''

import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(40))
print(sys.getrecursionlimit())
i = 0
def demo():
    global i
    i += 1
    print("Hello...", i)
    demo()

demo()