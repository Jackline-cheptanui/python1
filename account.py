from datetime import datetime
class Account:
    def __init__ (self,name,phone_number):
     self.name=name
     self.phone_number=phone_number
     self.balance=0
     self.statement=[]
     self.loan=0



    def show_balance(self):
      return f"saving have high interest{self.balance}"
    def deposit(self,amount):

        if amount>self.balance:
         return f"Hello {self.name}your balance is{self.balance}" 
        else:
         self.balance+=amount
         now=datetime.now()
         transaction= {
                 "amount":amount,
                  "time":now,
                   "Narration":"deposit"
             }
         self.statement.append(transaction)
         return self.show_balance()
   

         
    
    
    def withdraw(self,amount):
        
        if amount>self.balance:
            return f"hello balance is{self.balance} you cannot withdraw{amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            withdrawal= {
                 "amount":amount,
                  "time":now,
                   "Narration":"deposit"
             }
            self.statement.append(withdrawal)
            return self.show_balance()


    def show_statement(self):

        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")

    def borrow(self,amount,loan):
        if amount<=0:
            return f"Hello{self.amount} you have no loan" 
        elif (self.loan)>0:
            return f"Hello{self.amount}you will have a loan"
        elif amount<0.1:
            return f"Hello{self.amount}you do not qualify the loan"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            return f"Hello{self.amount}customer you have save {amount}"

    def repay(self,amount):
        if amount<0:
            return f"Hello{self.loan} you are to repay your {amount}" 
        elif amount<self.loan:
                self.loan-=amount
                return f"Hello {self.loan} dear customer you have repay your {amount}"
        elif amount > self.loan:

            diff=amount-self.loan
            self.loan = 0
            self.deposit(diff)
            now=datetime.now()
            transaction= {
                    "amount":amount,
                    "time":now,
                   "Narration":"deposit"
             }
            self.statement.append(transaction)
            return f"Dear customer you have repay successfully{self.deposit}"


