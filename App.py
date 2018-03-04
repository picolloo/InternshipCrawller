import User
import Crawller

class App:
    def __init__(self):
        self.crawller = Crawller.Crawller()
        self.users = []

    def insertUser(self, _name, _email, _course):
        self.users.append(User(_name, _email, _course))


app = App()