import os

path="/home/satyx/Downloads/"
files=os.listdir(path)

for i in files:
    temp=i[:11]
    if temp=="DAA_Lecture":
        print('Deleting file',i)
        os.remove(path+i)
