import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse();
st=''.join(str(i)+" " for i in arr)

print(st) 
