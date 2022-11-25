'''
This program is done by Anumakonda Sai Venkata Dhanush 
Roll No : CS20B1057
Binary Search
'''
l=0 #low
h=n-1 #high

myList=[]

for i in range(0,n):
    x = input("Enter the elements: ")
    myList.append(int(x))
j=n-1
print(myList)
for i in range(n):
    for j in range(0,n-i-1):
        if(myList[j]>myList[j+1]):
            temp = myList[j]
            myList[j] = myList[j+1]      #bubble sort
            myList[j+1] = temp
print("Sorted List is : ")
print(myList)

x = int(input("Enter the elements to be searched : ")) #taking search element
flag =0

#searching
for i in range(1,n):
    mid =(l+h)//2   #mid value updates after each iteration
    if(x == myList[mid]):
        flag=1
    elif(x <= myList[mid]):
        h = mid-1
    elif(x>myList[mid]):
        l = mid+1
    

if(flag==1):    
    print(f"The element {myList[mid]} is found at index {mid} ")
else:
    print("Element not present!")
