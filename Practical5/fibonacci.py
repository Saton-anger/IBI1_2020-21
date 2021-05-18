# initialize the series, give the original two words
a=1
b=1
print(a)
print(b)
# loop
for i in range(0,11):
	c=b
	b=a+b
	a=c	
	print(b)
