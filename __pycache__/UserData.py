import pandas as pd
from os.path import exists


class UserData:
    def __init__(self, file):
        self.file = file
        if exists(file):
            self.df = pd.read_csv(file)
        else:
            self.df = pd.DataFrame(columns=["email",  "psw"])
            self.df.to_csv(file)
        

    def getuser(self, mail):
        return list(self.df[self.df["email"] == mail])

    def contains(self, mail):
        print(len(list(self.df[self.df["email"] == mail])) < 1)
        return len(list(self.df[self.df["email"] == mail])) < 1

    def adduser(self, **user):
        print(user)
        if not user["email"] or not user["psw"]:
            return False
        user = pd.DataFrame({"email": [user["email"]], "psw": [user["psw"]]})
        self.df = pd.concat([self.df, user]).reset_index()
        print(self.df)

        self.save()
        return True

    def removeuser(self, mail, save=False):
        index = list(self.df["email"]).index(email)
        self.df = self.df.drop(index).reset_index()
        if save:
            self.save()

    def save(self):
        self.df.to_csv(self.file)

    def checkpassword(self, email, psw):
        psw = list(self.df[self.df["email"] == email]["psw"])
        if len(psw) < 1:
            return False
        return True if psw in psw else False