class point:
    def _init_(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def _repr_(self):
        output=""
        for i in self.data:
            output+=str(i)+""
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
            
            
