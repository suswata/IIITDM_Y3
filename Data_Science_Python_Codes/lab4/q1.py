txt = "welcome to the jungle"
word = "ta"
x = txt.split()
for row in x:
	if row.find(word) == 0:
		print("String exists!")
    elif row.find(word) != 0:
		print("String does not exists!")
   
        

print(x)
txt = "welcome to the jungle"
word = "ta"
x = txt.split()
for row in x:
	if(row.find(word) == 0):
		print("String exists!")
    elif(row.find(word)!=0):
		print("String does not exists!")
print(x)
