x = 100
def outer():
    global x
    x = x + 10
    #x = 8 #local variable
    print(x)
#print(x)
outer()