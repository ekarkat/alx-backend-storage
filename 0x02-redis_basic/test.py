def my_decorator(func):
	def wrapper(*args, **kwargs):
		print("Before calling the function")
		result = func(*args, **kwargs)
		print("After calling the function")
		print(func.__qualname__)
		return result
	return wrapper


class MyClass:
    def __init__(self):
        pass


    @my_decorator
    def my_method1(self, x, y):
        return x + y

    @my_decorator
    def my_method2(self, x, y):
        return x * y

# Create an instance of MyClass
obj = MyClass()

# Call the decorated methods
result1 = obj.my_method1(3, 5)
result2 = obj.my_method2(3, 5)

print("Result of my_method1:", result1)
print("Result of my_method2:", result2)