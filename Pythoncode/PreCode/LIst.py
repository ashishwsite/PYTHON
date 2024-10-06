# list is similar to array but is very easy then array
# 1 PUT DIFFENT TYPE OF DATA IN SAME LIST
# 2 LIST SYMBOL IS EMPTY LIST LIKE  list=[]
data = ["ramashish", 2001, "btech", 'm']
# print(data)
###
# 1 TRAVERSING LIST SIMIR AS FOR AUTO I
# 2  : =in colon is similr to in
# for item in data:
#     print(item)
# TO INSERT IN LIST AT LAST POSTINE   used append() function parameter (item)
data.append("dtu")
for item in data:
    print(item)
# ACCESING LIST ITEM AT SPECIFIC POSTION SIMILAR TO ARRAY METHEOD
   #  1 DATA[1],DATA[0]
# INSERTING IN THE LIST AT SPECIFIC POSTION  by using insert() function parametr (postion ,item)
data.insert(1, "kumar")
# COUNT NUMBER OF PARTICULAR ITEM  PRESENT IN THE LIST BY USING COUNT () FUC=NTTION PARAMETE (ITEM_WHOSE_COUNT_WANT)
ans = data.count(22)
print(ans)
# LENGTH OF LIST BY  USING LEN() FUN PARMATE (NAMEOFLIST)
L = len(data)
print(L)
# sorting of list using sort() function   parmater (none)
data.sort()
# sort list in decreasing orde usig reverse() fun  paramete (none)
data.reverse()
# SLICING OF LIST USSING SIMPLE WAY LIKE NEWLIST=LIST[STAETINDEX:END_INDEX_NOTINCLUDE]
newlist = list[0:5]

