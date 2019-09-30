class vehicle:
    def _init_(self,doors,wheels,name):
        self.doors=doors
        self.wheels=wheels
        self.name=name
    def _repr_(self):
        return "%s: %d doors and %d wheels"%(self.name, self.doors, self.wheels)
    def _eq_(self,aveh):
        return self.doors==aveh.doors and self.wheels==aveh.wheels
    def _iadd_(self,aveh):
        self.doors+=aveh.doors
        self.wheels+=aveh.wheels
        self.name+="+"
        self.name+=aveh.name
        return self
