import os

print("Location:-")
print("1.Enter the location\n2.Current Location")
inp=int(input('Enter your choice:'))


if inp==1:
	location=input("Enter the location")		#Input of location
	if os.path.exists(location)==False:		#Checking if path exists
		print("Invalid Address")
		print("Terminated!!!!!")
		exit()
elif inp==2:
	location=os.getcwd()				#Location of Current Working Directory
else:	
	print("Invalid Input")
	print("Terminated!!!!!")
	exit()


files=os.listdir(location)

print("\nQuantity of files:-")
print('1. Just one file\n2. Entire Directory')
inp=int(input("Enter your choice:"))

if inp==1:
	name=input("Enter filename with extension:")
	if os.path.exists(name):			#Checking if file exists
		new_name=input("Enter the new name of the file:")
		os.rename(name,new_name)
	else:
		print("Invalid Input")
		print("Terminated!!!!!")
		exit()
elif inp==2:
	print('\nStyle of renaming')
	print("1.Change the entire filename in Capital Letters\n2.Change the entire filename into Small Letters\n3.Alter the letters from small to capital or vice-versa")
	ch=int(input('Enter your choice:'))

	if ch==1:
		for i in files:
			pos=i.find('.')
			if pos!=-1:
				extension=i[pos:]
			else:
				extension=''
			os.rename(i,i[:pos].upper()+extension)		#Renaming Files
	
	elif ch==2:
		for i in files:
			pos=i.find('.')
			if pos!=-1:
				extension=i[pos:]
			else:
				extension=''
			os.rename(i,i[:pos].lower()+extension)		#Renaming Files

	elif ch==3:
		for i in files:
			new_name=''
			pos=i.find('.')
			if pos!=-1:
				extension=i[pos:]
			else:
				extension=''
			for j in i:
				if j=='.':
					break
				elif ord(j)>=65 and ord(j)<=90:
					new_name=new_name+chr(ord(j)+32)
				elif ord(j)>=97 and ord(j)<=122:
					new_name=new_name+chr(ord(j)-32)
				else:
					new_name=new_name+j
			new_name=new_name+extension			
			os.rename(location+'/'+i,location+'/'+new_name)		#Renaming files
	else:
		print("Invalid Input")
		print("Terminated!!!!!")
		exit()

else:
	print("Invalid Input")
	print("Terminated!!!!!")
	exit()
