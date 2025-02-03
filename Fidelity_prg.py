data=100
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def reverse_num(num):
    while num!=0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num//=10