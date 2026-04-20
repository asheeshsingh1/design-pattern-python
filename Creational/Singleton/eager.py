# Class implementing Eager Loading
class Eager:
    __instance = None

    def __init__(self):
        if Eager.__instance is not None:
            raise Exception("Instance already Created")
        Eager.__instance = self

    @staticmethod
    def getInstance():
        return Eager.__instance
    

Eager._Eager__instance = Eager()
print(Eager.getInstance()) # Instance printed

# Throws Exception for instance already created
Eager._Eager__instance = Eager()