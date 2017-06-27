import sys


arr = []
lis=[]
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp) 
i=0
j=0
for i in range(4):
    for j in range(4):
        tot = 0
        for p in range(i,i+3):
                for q in range(j,j+3):
                    tot = tot + arr[p][q]
                    q=q+1
                p=p+1
        tot=tot-((arr[i+1][j])+(arr[i+1][j+2]))  
        lis.append(tot)
        j=j+1
    i=i+1        
maximum=max(lis)
print maximum
