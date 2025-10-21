list1=[]
n=int(input("Enter the limit:"))
for i in range (n):
    num=int(input("Enter the number: "))
    list1.append(num)
print("List:",list1)
print("Positive Numbers:")
for x in list1:
    if (x>0):
        print(x)
