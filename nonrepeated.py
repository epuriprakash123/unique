def repeat(x):
	r=[]
	for i in range(n-1):
		for j in range(i+1,n):
			if x[j]==x[i]:
				if x[j] not in r:
					r.append(x[j])
	return r			
n=int(input())
l=list(map(int,input().split()))
k=repeat(l)
for i in range(n):
	if l[i] not in k:
		print(l[i])
