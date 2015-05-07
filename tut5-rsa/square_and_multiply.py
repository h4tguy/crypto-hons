n,b,d=map(int,raw_input().split())
exp=1
res=6
coeff=[]
pows=[]
while(exp<=d):
	exp*=2
	if(d%exp!=0):
		d-=exp/2
		coeff.append(1)
	else:
		coeff.append(0)
	pows.append(res)
	print pows[-1],coeff[-1],exp/2
	res=(res**2)%n
print reduce(lambda x,y:x*y,(i[1]**i[0] for i in zip (coeff,pows)),1)%n
