class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logs = []  # instance-level logs
        return cls._instance

    def log(self, message):
        self._logs.append(message)

    def get_logs(self):
        return self._logs

logger1 =Logger()
logger2 =Logger()

print(logger1 is logger2)   
logger1.log("first message")
print(logger1.get_logs())

logger2.log("second message")
print(logger2.get_logs())


