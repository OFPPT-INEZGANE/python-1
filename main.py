"""
# Lambda Function

x = lambda a : a **2

print(x(3))

# Nested function

def Login(n):
    return lambda a : a - n


print(Login(1)(10))


# Sorted Uses

list = ["a" , "c" , "b"]
x = sorted(list)
print(x)


# Sort Uses

list.sort()
print(list)



a=["k","h","m","p"]
a.sort(reverse=False)
print(a)


def pair(a):
    return a + 1


x = map( pair , [1,5,9])


print(list(x))

"""





++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Filter

Points = [10 , 15 , 19.75 , 14 , 3 , 2.5 , 13]

def pointFilter(point):

    if point >= 10:
        return Point
   

filterdList = filter(pointFilter, Points)

for x in filterdList:
  print(x)
