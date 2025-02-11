

class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero("Деление на ноль не возможно", {"a": a, "b": b})
    return a / b

try:
    result = f(10, 1)
except ProZero as e:
    print("не очень хороший деньб мы поймали ошибку")
    print(f"Сообщение об ошибке: {e.message}")
    print(f"Дополнительная информация: {e.extra_info}")