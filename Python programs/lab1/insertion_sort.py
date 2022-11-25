#insertion sort
n = int(input("Enter size of list :  ")) #taking size input

myList=[] 
count=0
#taking list elements
for i in range(n):
    x = input("Enter the elements: ")
    myList.append(int(x))
print(myList)
size = len(myList)

for i in range(1,size):
    j = i-1
    num = myList[i] #initializing num with a[1] first

    while j>=0 and num<myList[j]:       #if num < mylist[j]

        myList[j+1] = myList[j]
        
        j = j-1             #decrementing index j to sort any previous num values

    myList[j+1] = num   #updating jth index each time with num

print("The sorted array is : ")
print(myList)

