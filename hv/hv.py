def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Error during calculation: {e}")
            return None    return wrapper

result1 = calculate("2 * 85")
print(result1)

result2 = calculate("10 / 0")
print(result2)def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Error during calculation: {e}")
            return None    return wrapper

result1 = calculate("2 * 85")
print(result1)

result2 = calculate("10 / 0")
print(result2)