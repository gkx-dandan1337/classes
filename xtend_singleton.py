class Tracker:
    _instance = None
    init_count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            Tracker.init_count += 1
            print("Initializing...")
            self._initialized = True

a = Tracker()
b = Tracker()

print(a is b)                # True
print(Tracker.init_count)    # 1
