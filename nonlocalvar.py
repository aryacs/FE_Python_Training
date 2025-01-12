
def Out():
    x = 25 #non local variable
    print(x)
    def In():
        nonlocal x
        x = x / 5
        print(x)
        x = 200 #local variable
        print(x)
    In()
Out()
