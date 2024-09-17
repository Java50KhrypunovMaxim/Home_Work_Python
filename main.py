def repeat_decorator(repeat_count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeat_count):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def example_function():
   print("Hello")


example_function()
