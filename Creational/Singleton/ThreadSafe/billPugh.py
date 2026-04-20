# Class implementing Singleton using holder-like lazy initialization
class Singleton:
    # Private constructor simulation
    def __init__(self):
        if hasattr(Singleton, "_created"):
            raise Exception("This class is a singleton!")
        Singleton._created = True

# Function acting like a static holder in Java
def getInstance():
    # This behaves like Java's Holder class:
    # - Singleton instance is not created until getInstance() is first called
    # - The attribute is only added once (lazy initialization)
    # - Thread-safety is not guaranteed unless protected externally
    if not hasattr(getInstance, "_instance"):
        getInstance._instance = Singleton()
    return getInstance._instance