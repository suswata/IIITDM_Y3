'''
This program is done by Anumakonda Sai Venkata Dhanush 
Roll No : CS20B1057

'''
mydict = dict("")
temp = True
while(temp):
    print("1.Create Empty set \n"
    "2.Insert\n"
    "3.Delete\n"
    "4.Search\n"
    "5.Print\n"
    "6.Union\n"
    "7.Intersection\n"
    "8.Set Difference\n"
    "9.Symmetric Difference\n"
    "10.Exit\n")
    choice = int(input("Enter the choice : "))
    if(choice == 1):
        dummy = input("Enter the name of the set : ")
        mydict[dummy]={}
        print("Empty set as been created !")
        print(mydict)
    elif(choice ==2):
        n = int(input("Enter the number of elements in the set : "))
        print(mydict)
        name_set = input("Enter the name of the set : ")
        myset=set()
        mylist = []
        step = int(0)
        while(step+1<=n):
            
            if(name_set in mydict):
                val = input(f"Enter the value - {step+1} : ")
                mylist.append(val)
                step = step+1
        myset.update(mylist)
        mydict[name_set] = myset
        print(myset)
        print(mydict[name_set])    
        print(f"{mydict[name_set]} has been inserted ")  
    elif(choice == 3):
        temp1 = input("Enter the name of set to delete (key) : ")
        if(temp1 in mydict):
            print(f"set {temp} : {mydict[temp1]} has been deleted!")
            del mydict[temp1]
            print(mydict)
        else:
            print("Element not present")
    elif(choice ==4):
        temp = input("Enter the name of the set to search : ")
        if(temp in mydict):
            print(mydict[temp])
    elif(choice==5):
        print(mydict)
    elif(choice == 6):
        n = int(input("Enter the number of sets for union : "))
        templist = []
        for i in range(n): 
            temp = input("Enter the the set names  : ")
            if(temp in mydict):
             templist.append(mydict[temp])
        
        print("After Union : ")
        print(set().union(*templist))
    elif(choice == 7):
        n = int(input("Enter the number of sets for intersection : "))
        templist = []
        for i in range(n): 
            temp = input("Enter the the set names  : ")
            if(temp in mydict):
             templist.append(mydict[temp])
        
        print("After Intersection : ")
        print(set().intersection(*templist))
    elif(choice == 8):
        n = int(input("Enter the number of sets for Set Difference : "))
        templist = []
        for i in range(n): 
            temp = input("Enter the the set names  : ")
            if(temp in mydict):
             templist.append(mydict[temp])
        
        print("After Set Difference : ")
        print(set().difference(*templist))
    elif(choice == 9):
        n = int(input("Enter the number of sets for Symmetric Difference  : "))
        templist = []
        for i in range(n): 
            temp = input("Enter the the set names  : ")
            if(temp in mydict):
             templist.append(mydict[temp])
        
        print("After Symmetric Difference  : ")
        print(set().symmetric_difference(*templist))
    elif(choice == 10):
        break
        
        
