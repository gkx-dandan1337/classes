class DataBaseConnection:
    _instance = None
    _allow_init = False 

    def __new__(cls):
        if not cls._allow_init:
            raise ValueError('bruh')    
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._allow_init = True 
            cls._instance = cls()
            cls._allow_init = False 
        return cls._instance

    def __init__(self):
        print("Connecting to the database..")

db = DataBaseConnection.get_instance()


