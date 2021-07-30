# def show(min,max):
#     print(min)
#     if min == max :
#         return
#     else :
#         show(min+1,max)
# show(1,10)

# def sum(min,max):
#     if min == max :
#         return max
#     else:
#         return min + sum(min+1,max)
# result =sum(1,10)
# print(result)

# sum(1,3):
#     1+sum(2,3)
#       2+sum(3,3)
#       2+3
#     1+5
# 6

# def pow(x,y):
#     if y == 0 :
#         return 1
#     else :
#         return x*pow(x,y-1)
# result = pow(3,4)
# print(result)

# def gcd(x,y):
#     if abs(x-y) == min(x,y):
#         return min(x,y)
#     else :
#         gcd(abs(x-y),min(x,y))
# result = gcd(9,6)
# print(result)

# def gcd(x,y):
#     if x == y:
#         return min(x,y)
#     else :
#         return gcd(abs(x-y),min(x,y))
# result = gcd(9,6)
# print(result)

def fib(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1)+fib(n-2)

result = fib(99)
print(result)