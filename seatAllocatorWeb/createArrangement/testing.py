path = 'C:\\Users\\DELL\\Desktop\\seatAllocatorWeb\\file2.py'
l1 = list()
fp1 = open(path, 'r')
for line in fp1:
    for word in line.split():
        l1.append(word)
print(l1)
