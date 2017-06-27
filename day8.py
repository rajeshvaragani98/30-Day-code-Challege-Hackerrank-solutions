n=int(raw_input())
book={}
for i in range(n):
    temp=(raw_input()).split()
    book[temp[0]]=temp[1]
for i in range(n):
    s=raw_input()
    if s in book:
      print s + '='+ book[s]
    else:
      print "Not found"
