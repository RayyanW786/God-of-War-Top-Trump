from user import UserUtils

class Launcher(object):
    pass

class Menu(object):
    def __init__(self):
        self.userutils = UserUtils()
        self.first_menu()

    def first_menu(self): #displays menu and allows users to log in, register or start the game, log out or view stats
        while True:
            try:
                try:
                    getattr(self, "logged_in")
                    user_input = input(
                        "\n____________________\n1. Start Game\n2. Log Out 1-2: ")
                    user_input = int(user_input)
                    if user_input == 1:
                        pass
                    elif user_input == 2:
                        delattr(self, "logged_in")
                        print("You have been Logged out...")
                    #elif user_input == 3:
                    #    self.get_stats()


                except AttributeError: #getattr raises AttributeError when the Attribute doesnt exist
                    user_input = input(
                        "\n____________________\n1. Register\n2. Log in\n___________________\nEnter your choice 1-2: ")
                    user_input = int(user_input)
                    if user_input == 1:
                        self.user_creation()
                    elif user_input == 2:
                        self.login()
                    else:
                        print("Please enter a valid option\nTo quit type quit, exit or stop!")
            except ValueError: #value error means the program doesnt stop if they input a non integer type
                if str(user_input).lower() in ["quit", "exit", "stop"]:
                    exit()

    def user_creation(self):
        while True:
            username = input("enter a username: ")
            if self.userutils.lookup(username):
                print("Invalid: Username Taken!")
            else:
                break #username is not in current data

        if username.lower() == "exit": #they exited and so we return None
            print("exiting...")
            self.first_menu()
        while True:
            password = input("enter a password: ")
            if self.userutils.register_checks(username, password):
                break
            else:
                if password.lower() == "exit":
                    print("exiting...")
                    self.first_menu()
        res =  self.userutils.register(username, password)
        if res == True:
            self.logged_in = True
        else:
            print("Account Creation Failed")
        self.first_menu()

    def login(self):
        res = False
        while not res:
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            res = self.userutils.login(username, password)
            if username.lower() == "exit" or password.lower() == "exit":
                print("exiting...")
                self.first_menu()
            if not res:
                print("Incorrect Username or Password")
        if res == True:
            self.logged_in = True
        self.first_menu()

if __name__ == "__main__":
    Launcher()
