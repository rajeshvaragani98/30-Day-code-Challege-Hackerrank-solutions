    def computeDifference(self):
        maxi=0
        l=len(self.__elements)
        for i in range(l):
            for j in range(i+1,l):
                temp=abs(self.__elements[i] - self.__elements[j])
                maxi=max(temp,maxi)
        self.maximumDifference=maxi       
