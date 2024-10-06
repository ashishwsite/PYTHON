t = 5
i = 1
data = int(input("enter your age to get some eligibility in india  about you  "))
if (data < 0):
    print("invalid age is never negative ")
elif ((data > 0) & (data < 18)):
    print("yore are kid at this age ")
elif (data > 18):
    print("youe aarea eligible to vote and drive ")
# elif:
#         print("your are in age limit of teeneager doyour study seriously ")
else:
    print("your are senior citizen ")
