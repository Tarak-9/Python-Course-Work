class Instagram:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created! parent-1")

class InstaV1:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created! parent-2")

class InstaV2(Instagram,InstaV1):
    def __init__(self,username):
        Instagram.__init__(self,username)
        InstaV1.__init__(self,username)
        print("Creating users from version3")


i=InstaV2("username--Xyz")
