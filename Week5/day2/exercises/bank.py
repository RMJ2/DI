class Bank():                                           
    def __init__(self, account, pin):                   #initialise parameters
        self.account = account                          
        self.pin = pin 
        self.balance = 0                                # value for starting balance
        self.history = []                               # empty list to store history of deposits and withdrawels. 

    def deposit(self, amount): 
        if amount <= 0:                                 # to ensure no negative deposit can be made
            print('You must deposit a positive amount')
        else:
            self.balance += amount                      # new balance, made by amount deposited
            self.history.append(f'Deposit: {amount}')   # update list of history for amount deposited. 

    
    def withdraw(self, amount):
        if amount > self.balance:                       #to ensure no withdrawal of negative funds is made
            print('You do not have enough funds')
        else:
            self.balance -= amount                      # new balance, made by amount withdrawn
            self.history.append(f'Withdraw: {amount}')  # update history listfor amount withdrawn
            return amount                               # returns amount in terminal


    def show_balance(self): 
        print(self.balance)                             # print balance


    def show_history(self):                             # 
        for thing in self.history:                      # item in list (instead of printing on one line) 
           print(thing)                                 # prints item line by line 


b1 = Bank(12345, 54321)
b1.deposit(100)
b1.deposit(100)
b1.withdraw(30)