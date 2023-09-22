
import re
s = "I had a dog and I used to take him on a walk everyday"

d = re.findall('dog|him', s)
print(d)


# l = [7,7,8,7,6]
# d = sorted(l)
# print(d)
# smax = d[-1]
# for esch in range(len(d)-1,-1,-1):
#     if(d[esch]!=smax):
#         smax = d[esch]
#         print(smax)
#         break


