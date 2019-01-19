from django.test import TestCase
from createArrangement.views import getobjects3,getobjects2,getobjects1
# Create your tests here.
getobjects3()
path = 'C:\\Users\\Vanitha\\Downloads\\seatAllocatorWeb\\file3.py'
l3 = list()
fp3 = open(path, 'r')
for line in fp3:
    for word in line.split():
        l3.append(word)
print(l3)
g=0
pop=l3[g]
if pop=='y':
    print("inside pop")
