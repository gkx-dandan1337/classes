import threading

class ConfigManager:
    _instance = None 
    _lock = threading.Lock()

    def __new__(cls): #ensures a singleton is created.
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
# Simulate multithreaded usage
def create_instance():
    instance = ConfigManager()
    print(id(instance))

threads = [threading.Thread(target=create_instance) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]


    