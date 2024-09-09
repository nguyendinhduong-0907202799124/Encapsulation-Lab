class Email_Validator:
    def __init__(self,min_length:int,mails:list,domains:list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains 

    def validate(self,mail:str):
        self.mail = mail
        A,B=mail.split('@')
        B,C = B.split('.')
        if len(A)>=self.min_length and B in self.mails and C in self.domains:
            return True
        else:
            return False

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = Email_Validator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
