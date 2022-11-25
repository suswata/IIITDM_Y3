#Done by CS20B1057
#ANUMAKONDA SAI VENKATA  DHANUSH
'''
Write a python script to implement student details using a dictionary.
 The roll number of the student will be the key,
  the value will be a list containing the name, CGPA, and mobile number of the respective student. 
  The program should be implemented as a menu-driven program with the following menus,
Insert
Delete
Search
Exit
'''

mydict = dict("")
x = int(input("Enter the number of students : "))
print(f"Here are the list of {x} students")
temp =True
count = int(0)

while(temp):
    print("1. Insert\n"
    "2.Delete\n"
    "3.Search\n"
    "4.Exit\n");
    choice = int(input("Enter the choice : "))

    if(choice == 1):
        
            roll_no = input(f"Enter the Roll No of student - {count+1} : ")
            name = input("Enter the name of the student : ")
            ph_no = input("Enter the phone number  : ")
            cgpa = input("Enter the CGPA : ")
            mylist=[]
            mylist.append(name)
            mylist.append(ph_no)
            mylist.append(cgpa)
            mydict[roll_no]=mylist
            count = count +1
            print(f"{roll_no} has been added successfully!\n")
            print(mydict)
        
    elif(choice ==2):
        if(len(mydict) == 0):
            print("No Elements to delete ! Insert Roll nos (keys)")
        else:
            dummy = input("Enter the key to delete : ")
            if(dummy in mydict):
                del mydict[dummy]
        print(mydict)
        
    elif(choice ==3):
        if(len(mydict) == 0):
            print("No Elements to delete ! Insert keys")
        else:
            loc = input("Enter the  roll no to search : ")
            for i in range(len(mydict)):
                if(loc in mydict):
                    print(f"Roll no {loc} found !!\n")
                    print(mydict[loc])
                    break
                else:
                    print("No key found !")
    else:
        print("Exiting code !")
        temp = False
        break
         
       
    
print("code works!\n")