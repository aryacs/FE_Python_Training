a = 50 #global namespace
def test():
    a = 10 #local namespace
    #print(a)
    print(dir())


def demo():
    b = 15
    #print(b)
    print(dir())
    def demoinner():
        c = 20
        #print(c)
    print(dir()) #enclosed namespace
    demoinner()

print(dir())
test()
demo()