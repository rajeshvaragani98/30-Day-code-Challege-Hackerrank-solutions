import sys

n = int(raw_input().strip())
n_b=str(bin(n))[2:]
n_l=len(n_b)
count=0
result=0
i=0
for i in range(n_l):
    if(n_b[i]=='1'):
        count=count+1
        result=max(result,count)
    else:
        count=0
print result    
