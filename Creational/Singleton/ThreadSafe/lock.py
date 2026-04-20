import threading

# Class implementing thread-safe Singleton
class Singleton:
    # Object declaration
    __instance = None

    # Lock for thread safety (similar to Java's 'synchronized')
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method to get the instance of class
    @staticmethod
    def getInstance():
        # Only one thread can enter this block at a time
        # This is equivalent to using 'synchronized' in Java
        with Singleton.__lock:  # Synchronized block
            if Singleton.__instance is None:
                Singleton()
        return Singleton.__instance
