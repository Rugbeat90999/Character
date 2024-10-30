class MoneyError(BaseException):
    def __init__(self, message):
        print(f"Money Error: {message}")