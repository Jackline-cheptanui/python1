# class Bank:
#     type="m-shwari"
# def __init__ (self,name,save):
#     self.name=name
#     self.save=save

# def suggestion(self):
#     return f"offer low intrest to user{self.name}"
# def loan(self):
#     return f"provide service to the consumer{self.save}"
class Bank:
    name="equity"

    def __init__ (self,name,phone_number):
     self.name=name
     self.phone_number=phone_number
     self.balance=0



     def show_balance(self):
      return f"saving have high interest{self.balance}"
    def borrowloan(self):
          return f" loan rate is at low rate{self.balance}"
    def update(self,amount):
        if amount>0:
            return{self.show_balance}
    def deposit(self,amount):
        self.balance+=amount
        return f"high amount to get more interest{self.deposit}" 
    def repay(self,amount):
        self.loan-=amount
        return f"hello welcome{self.name} you loan is{self.loan}shilling you have paid{amount}"
    def withdraw(self,amount):
        self.balance=amount
        if amount>self.balance:
            return f"hello balance is{self.balance} you cannot withdraw{amount}"
            else
            self.balance=amount



        
    
         


          
              
          
          
      
          
