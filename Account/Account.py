class Account:
    def __init__(self,balance=0): #قيمة الرصيد الافتراضية صفر في حال لم يدخل قيمة
        self.__balance = balance

    def deposit(self,balance): #لايداع مبلغ
        self.__balance+=balance

    def withdrow(self,balance):# لسحب مبلغ من الرصيد
        if self.__balance>balance:
            self.__balance -=balance
        else:
            print("Balance not enough !")
        
    def setBalance(self,balance):
         self.__balance=balance

    def getBalance(self):
        return f"The current balance : {self.__balance}"



