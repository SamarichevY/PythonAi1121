def robust_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Помилка обчислення: {e}")
            return None

    return wrapper

@robust_calculator
def calculate(expression):
    return eval(expression)

expression = "55 + 3"
result = calculate(expression)
print(f"Результат: {result}")