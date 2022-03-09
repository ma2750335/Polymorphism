from abstract import abstract

class FbLogin(abstract.Login):
    def __init__(self) -> None:
        self.Name = None
    
    def setAccoutName(self,name: str):
        self.Name = name

    def singout(self):
        print('fb {name} singout '.format(name=self.Name))
    
    def login(self):
        print('fb {name} login '.format(name=self.Name))

if __name__ == "__main__":
    fblogin = FbLogin()
    fblogin.setAccoutName('Sam')
    fblogin.singout()
    fblogin.login()
