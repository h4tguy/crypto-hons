def gcd(a,b):
	if(a<b):
		a,b=b,a
	if(b==0):
		return a
	return gcd(b,a%b)

# init is the initial value for the Pollard rho method
n,init=map(int,raw_input().split())
f=lambda q: (q**2+1)%n
x=f(init)
y=f(f(init))
i=1
while(gcd(abs(x-y),n)==1):
	print x,y
	x=f(x)
	y=f(f(y))
	i+=1
print x,y,gcd(abs(x-y),n)
