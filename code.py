class LoginReg:
    users={}
    loggedin=None
    
    def Register(self):
        if self.loggedin==None:
            username = input("Enter username:")
            rollno = input("Enter Rollno:")
            email = input("Enter Email:")
            password = input("Enter Password:")
            if rollno not in self.users.keys():
                self.users[rollno]=[username,email,password]
                print(rollno,"registration successful")
            else:
                print("User already exists")
        else:
            print("Logout to register")

    def Login(self):
        if self.loggedin==None:
            rollno = input("Enter Rollno:")
            password = input("Enter Password:")
            if rollno not in self.users.keys():
                print("User not found")
            elif password!=self.users[rollno][2]:
                print("Invalid Password")
            else:
                print("Login Succesful")
                self.loggedin=rollno
        else:
            print(self.loggedin,"already logged in")

    def display(self):
        if self.loggedin:
            rollno=self.loggedin
            print("Username: ",self.users[rollno][0])
            print("Rollno: ",rollno)
            print("Email: ",self.users[rollno][1])
        else:
            print("Login to display details")

    def logout(self):
        if self.loggedin:
            self.loggedin=None
            print("Successfully logged out")
        else:
            print("User already logged out")


#driver code
option=1
ob = LoginReg()

while option!=5:
    
    print("\nChoose one option: \n 1.Register\n 2.Login \n 3.Display details \n 4.Logout \n 5.Exit")
  
    try:
        option=int(input())
    except ValueError:
        print("Enter integer")
        continue
    
    if option==1:
        ob.Register()        
    elif option==2:
        ob.Login()
    elif option==3:
        ob.display()    
    elif option==4:
        ob.logout()
    elif option!=5:
        print("Enter a valid option (1,2,3,4,5)")

print("Program Terminated")

