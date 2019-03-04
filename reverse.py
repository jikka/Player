try:
	n=int(raw_input())
	i=0
	sum=0
	x=n
	while(n!=0):
		i=n%10
		sum=sum*10+i
		n=n/10
	print sum
		
except:
	print "Error"
