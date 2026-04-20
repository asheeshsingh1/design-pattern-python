import threading

# Class implementing double-checked locking Singleton
class Singleton:
    # Object declaration
    __instance = None
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method using double-checked locking
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:  # First check (no lock)
            with Singleton.__lock:
                if Singleton.__instance is None:  # Second check (with lock)
                    Singleton()
        return Singleton.__instance