"""A decorator program to do division"""


def div(a,b):
    """original function."""

    print(a/b)


def decorator_div(func):
    """Decorator function."""

    def inner(a,b):
        if a>b:
            a,b = b,a
        return func(a,b)
    
    return inner


call_decorator = decorator_div(div)

div(100,200)