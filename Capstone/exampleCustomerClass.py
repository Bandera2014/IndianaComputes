class Customer:
    def __init__(self,customer,username,password,savings,checkings,creditCard,pin):
        self.customer=customer
        self.username=username
        self.password=password
        self.savings=int(savings)
        self.checkings=int(checkings)
        self.creditCard=creditCard
        self.pin=pin


    def modifySavings(self,s):
        self.savings=s

    def modifyCheckings(self,c):
        self.checkings=c
    
    def modifyPin(self,p):
        self.pin=p


    def fileFormat(self):
        return f"{self.customer}, {self.username}, {self.password}, {str(self.savings)}, {str(self.checkings)}, {self.creditCard}, {self.pin}\n"