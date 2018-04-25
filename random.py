import hashlib
a=open("random.txt")
x=a.read()
a.close()
y=""
n=int(input("stringin uzunlugu kac olsun: "))
for i in range(0,n):
	x=hashlib.md5(x.encode('utf-8')).hexdigest()
	y=y+x[7]
print("hex: ",y)
print("dec: ",int(y,16))