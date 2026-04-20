# Class implementing Lazy Loading
class Lazy:
    __instance = None

    def __init__(self):
        if Lazy.__instance is not None:
            raise Exception("This class is a singleton!")
        Lazy.__instance = self

    @staticmethod
    def getInstance():
        if Lazy.__instance is None:
            Lazy()
        return Lazy.__instance