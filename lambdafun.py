# Lambda Function

#lambda a : a + 10 #function without name
add = lambda a : a + 15
print(add)
print(add(5))
print(type(add))


def addition(a, b):
    return a + b

print(addition(5,6))


addition = lambda a, b : a +b
print(addition(8,7))

#return multiple values
add= lambda a, b : (a +b, a - b)
add, sub = add(4,3)
print(add)
print(sub)

#diff arguments
add= lambda a, b =10 : (a +b, a - b)
add, sub = add(4)
print(add)
print(sub)


add= lambda a, b =10 : (a +b, a - b)
add, sub = add(a = 15)
print(add)
print(sub)
