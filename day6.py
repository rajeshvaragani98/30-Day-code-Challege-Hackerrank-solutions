import sys
n=int(raw_input())
for i in range(n):
    s=raw_input()
    n_s=len(s)
    even=[]
    odd=[]
    for j in range(n_s):
        if(j%2==0):
            even.append(s[j])
 
    for j in range(n_s):
        if(j%2==1):
            odd.append(s[j])
    even=''.join(even)
    odd=''.join(odd)
    print even,odd
