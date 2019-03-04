try:
	rom=str(raw_input())
	i=0
	k=0
	x=[]
	while(i<len(rom)):
		if(rom[i]=='I'):
			x.append(1)
		elif(rom[i]=='X'):
			x.append(10)
		elif(rom[i]=='L'):
			x.append(50)
		elif(rom[i]=='C'):
			x.append(100)
		elif(rom[i]=='D'):
			x.append(500)
		elif(rom[i]=='M'):
			x.append(1000)
		else:
			x.append(0)
			break
		i=i+1
	j=len(x)-1
	i=len(x)-1
	k=x[j]
	while(i>0):
		if(x[i]!=0):
			while(j>0):
				if(x[j]==x[j-1] or x[j]<x[j-1]):
					k=k+x[j-1]
				elif(x[j]>x[j-1]):
					k=k-x[j-1]
				else:
					pass
				j=j-1
			print k	
		else:
			print "Invalid"
			break
		i=i-1	
except:
	print "Invalid"
