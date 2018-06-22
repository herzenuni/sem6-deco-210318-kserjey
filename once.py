from functools import wraps

def once(func):
    wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.wrapped_func = func
            inner.result = func(*args, **kwargs)
            inner.called = True

        return inner.result
            
    inner.called = False
    return inner

@once
def initialize_settings():
    print("Settings initialized")
    return 25
    
print(initialize_settings())
print(initialize_settings())
print(initialize_settings.wrapped_func())
