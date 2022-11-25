#Done By CS20B1057
#A S V Dhanush
#Read Write Search of books in a library
n = int(input("Enter the number of books : "))
mybooks = []  # list of lists
step = n
while(1):
	print("1.Write\n2.Read\n3.Search\n4.Exit\n")
	opt = int(input("Enter Choice : "))
	if(opt == 1):
		if(step == 0):
			print("Overflow!")	#overflw condition
		else:
			f1 = open("myq1.txt", 'w') #opening a dummy txt file write mode
			while(step != 0):
				mylist = []
				x = input("Enter the ISSN (Unique): ")
				if(x not in mybooks):
					issn = x
				else:
					print("ISSN value already present!")
					break;
				title = input("Enter the book title : ")
				price = input("Enter the price : ")
				edn = input("Enter the edition : ")
				yr = input("Enter the year : ")
				aut_name = input("Enter the author name  :")
				mylist.append(issn)
				mylist.append(title)
				mylist.append(price)
				mylist.append(edn)
				mylist.append(yr)
				mylist.append(aut_name)
				print(mylist)
				mybooks.append(mylist)
				print(mybooks)

				for book in mylist:
					f1.write(book+'\t')
				f1.write('\n')
				step = step-1
			f1.close()
	elif(opt == 2):
		f1 = open("myq1.txt", 'r') #opening in read mode
		print("ISSN   TITLE    PRICE   EDN    YEAR    AUT_NAME")
		printfile = f1.read()
		print(printfile)
		f1.close()
	elif(opt == 3):
		f1 = open("myq1.txt", 'r')
		lines = f1.readlines()
		ser_word = input("Enter title to search : ")
		# print(lines)
		k = 0
		for line in lines:
			vals = line.split("\t")
			imp = vals[1]
			if ser_word == vals[1]:
				print(line)
				k+=1
				break
			else:
				continue
		if(k==0):
			print("Title Not found")
	else:
		break