# LEARN USIHG PRACTICE AND IMPLEMENTATION 
s='Sheher mein '
a='aeiouAEIOU'
for i in range(len(s)):
    # if(s.index(s[i])%2==0):
    # ^ s.index(char) give the index of char in the given string 
    if(i%2==0):
        print(i)
        if(s[i] in a):
            s=s.replace(s[i],'_')
print(s)  
# LEARN USIHG PRACTICE AND IMPLEMENTATION    
#PUTING VALU AT GIVEN INDEX
def fix(l):
    me=max(l)
    nl=[0]*(me+1)
    for i in l:
        nl[i]=i
    return nl    
l=list(map(int,input().split()))
# ^ MAP IS ESPACIALLY TO PUT ELEMENT IN LIST
# SPLIT( ) FUNCTION HELP TO TRAET AS WHITESPACE TO NEW NEW INPUI ARGUMENT 
nl=fix(l)
print(nl)