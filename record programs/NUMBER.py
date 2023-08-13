def PALINDROME(n):
    s=str(n)
    if s[::-1]==s:
        return 1
    else: 
        return -1
def SPECIAL(num):
    n=num
    s=0
    while n:
        i=n%10
        f=1
        for j in range(1,i+1):
            f*=j
        s+=f
        n=n//10
    if num==s:
        return 1
    else:
        return -1