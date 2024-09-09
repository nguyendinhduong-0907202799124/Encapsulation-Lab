class Account:
    def __init__(self,id:int,balance:int,pin:int):
        self.id=id
        self.balance=balance
        self.pin=pin
    def get_id(self,pins:int):
        self.pins=pins
        if self.pins==self.pin:
            return self.id
        else:
            return f'Wrong pin'
    def change_pin(self,old_pin,new_pin):
        self.old_pin=old_pin
        self.new_pin=new_pin
        if self.old_pin > self.new_pin:
            return f'Pin changed'
        else:
            return f'Wrong pin'

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))