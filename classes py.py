class emp:
    def create_emp(self):
        self.name=input("Enter Name")
        self.age=input("Enter Age")
        self.add=input("Enter address")
    def show_emp(self):
        print(self.name,self.age,self.add)

a=emp()
a.create_emp()
b=emp()
b.create_emp()

a.show_emp()
b.show_emp()


