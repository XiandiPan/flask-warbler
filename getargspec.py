import inspect

def my_function(a, b, c=0):
    pass

signature = inspect.signature(my_function)
parameters = signature.parameters

for name, param in parameters.items():
    if param.default != inspect.Parameter.empty:
        print(name, param.default)
    else:
        print(name, 'No default value')