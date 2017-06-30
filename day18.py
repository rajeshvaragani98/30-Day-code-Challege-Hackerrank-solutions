class Solution:
    # Write your code here
    
    def __init__(self):
        self.stack=[]
        self.queue=[]
    def pushCharacter(self,c):
        self.stack.append(c)
    def enqueueCharacter(self,c):
        self.queue.append(c)
    def popCharacter(self):
        temp=self.stack.pop()
        return temp
    def dequeueCharacter(self):
        temp=self.queue[0]
        del(self.queue[0])
        return temp
