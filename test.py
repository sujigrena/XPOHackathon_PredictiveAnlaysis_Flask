import natsort
import os
from random import randint

fi = open("filenames.csv","w")
fi1=open("Top_50_Products.csv","r")
j=0
for i,j in range(0,2),range(0,2):
	print(i,j)

val=natsort.natsorted(os.listdir("static/Product_Images/"))
print(val)
li=fi1.readlines()
print(li)
for i in range(len(val)):
	fi.write(val[i].split(".")[0]+",") #file name as names
	fi.write("/static/Product_Images/"+val[i]+",")
	#if(j%5==0):
	#	fi.write(str(j*50))
	#else:
	#	fi.write(str(randint(0, 99)))
	fi.write(li[i].split(',')[1].split('\n')[0])
	fi.write("\n")
	#j+=1

fi.close()
fi1.close()
