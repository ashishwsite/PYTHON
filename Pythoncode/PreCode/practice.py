# let a=30 by input 
a=input() 
# HERE 'A' TAKE VALUE IN STRING  AND  CALUCULATE ITS ACSII VALU WHILE USING IN THE FORM OF INTEGER
b=a*2
print(b)
import string 
import random
# HERE 'a' VARIBLE STORE a stirng consiting of all alpbates of lower and upper case
a=string.ascii_letters
# a=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(a)
n=6
for i in range (n):
    l=[]
    for j in range(n):
       l.append(random.choice(a))

    for e in l:
        print(e ,end=' ')
# SOME FUNCTION UNDERSATAND
def uniqueE(L):
    ans = list()
#   ^list()  is way  of creating empty list
    for a in L:

        if L.count(a) == 1:
            #   ^ L=list_name, count = is function which checking occerng of element , a=element
            ans.append(a)
    return (sorted(ans))
# SOME FUNCTION UNDERSATAND
def count_letters(S):
    ans = {}
    # ^ ans =dictorory/object store key_valu
    for j in S:
        if j in ans:
            # ^   if j in ans: help to checking the presence of j (element) in ans
            ans[j] += 1
            # ^ ans[j]+=1 is way of creating increasing value
        else:
            ans[j] = 1
            #^ ans[j]=1 is way of creating new key_valu in dictionary
    return (ans)
# SOME FUNCTION UNDERSATAND
def fun(n):
    if(n==1):
        return 1
    return n(n-1)
#^ yaha paar default parameter ko dekh kar function calll ho gayga
n=5
print(fun(n))        
# LEARN AFTER IMPLEAMANTATION 
word="facebook"
new=''
for w in word:
    i=ord(w)
    #^ ord() which help in convert in lower case 
    j=(((i+26)-97)%26)+97
    new=new+chr(j)
print(new)  