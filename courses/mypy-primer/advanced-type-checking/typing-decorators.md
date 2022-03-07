---
title: Type checking decorators
include_in_preview: false
---

Decorators are functions that usually wrap other functions with some extra code.

How they do it is by replacing a function with a wrapper function. This "wrapper
function" calls the original function inside it, but adds extra code above and
below it.

For example, take this decorator that just logs everytime you call a specific
function:

```{.python .example .mypy-strict}
def log(function):
    """Log everytime you call the function"""
    def wrapper():
        print(f"Calling the function!")
        function()
    
    return wrapper

@log
def fortytwo():
    print(42)

fortytwo()
```

The `@log` decorator wraps the `fortytwo` function such that everytime you call
it, it prints out `Calling the function!`. And the best part is that you can use
the same `@log` decorator on many functions, and it'll work on all of them.

So, how do we add type hints to this function? We've already seen one method to
do this: use a `Protocol`:

```{.python .example .mypy-strict}
from typing import Protocol

class LogFunction(Protocol):
    def __call__(self) -> None: ...

def log(function: LogFunction) -> LogFunction:
    """Log everytime you call the function"""
    def wrapper() -> None:
        print(f"Calling the function!")
        function()
    
    return wrapper

@log
def fortytwo() -> None:
    print(42)

fortytwo()
```

But it becomes clear very quickly that this code needs some fixes, when you try
to call it with a function that takes arguments:

```{.python .example .mypy-strict}
from typing import Protocol

class LogFunction(Protocol):
    def __call__(self) -> None: ...

def log(function: LogFunction) -> LogFunction:
    """Log everytime you call the function"""
    def wrapper() -> None:
        print(f"Calling the function!")
        function()
    
    return wrapper

@log
def get_greeting(name: str, age: int, location: str) -> str:
    return f"Hi, I am {name}, {age}, from {location}."

greeting = get_greeting("Steve", 27, "London")
print(greeting)
```

Running the code (and also while checking through mypy), we realise that we have
hard-coded the function being passed-in to have no arguments, and to have no
return value:

```python
    def wrapper() -> None:
        print(f"Calling the function!")
        function()
```

Meanwhile right now, we want to pass a function that can take 3 arguments and
also return a string.

We could update our protocol to handle this:

```python
class LogFunction(Protocol):
    def __call__(self, name: str, age: int, location: str) -> str: ...
```

Or we could ditch the protocol completely and use the generic `typing.Callable`:

```python
from typing import Callable

def log(function: Callable[[str, int, str], str]) -> Callable[[str, int, str], str]:
    def wrapper(name, age, location) -> str:
        print(f"Calling the function!")
        return function(name, age, location)
    
    return wrapper
```

But the main problem still remains: We want to be able to pass functions with
*any* function signature, not any pre-defined one.

You can do that by replacing `function(name, age, location)` with
`function(*args, **kwargs)`, and then making a `Callable` type that can accept
any number of any arguments and return anything. This is how you do it:

```python
from typing import Any, Callable

def log(function: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling the function!")
        return function(*args, **kwargs)
    
    return wrapper


@log
def fortytwo() -> None:
    print(42)

@log
def get_greeting(name: str, age: int, location: str) -> str:
    return f"Hi, I am {name}, {age}, from {location}."


fortytwo()
greeting = get_greeting("Steve", 27, "London")
print(greeting)
```

The `...` used as the first argument of `Callable[..., Any]` tells mypy that you
want the function to be able to accept as many arguments of any type as needed.

Though there's just one problem with this, note that we're saying the decorated
function returns `Any`. This means that if you return something from a decorated
function, even if that function had types, the types are now gone. This is a
phenomenon called "type erasure", and it can creep up in your applications if
you start using `Any` in a lot of places.

For decorators however, usually they don't change the signature of a function.
So we can just make the decorator generic, to allow it to work with any callable
type:

```{.python .example .mypy-strict}
from typing import Any, Callable, TypeVar

T = TypeVar('T', bound=Callable[..., Any])

def log(function: T) -> T:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling the function!")
        return function(*args, **kwargs)
    
    return wrapper  # type: ignore


@log
def fortytwo() -> None:
    print(42)

@log
def get_greeting(name: str, age: int, location: str) -> str:
    return f"Hi, I am {name}, {age}, from {location}."


fortytwo()
greeting = get_greeting("Steve", 27, "London")
print(greeting)
```

Doing `reveal_type(greeting)` here should successfully tell the type `int`.

`T = TypeVar('T', bound=Callable[..., Any])` tells mypy that we want `T` to be
any type, as long as it falls within being `Callable[..., Any]`. Essentially, we
are saying we want `T` to accept any callable type.

Notice that `wrapper()` still has to use `Any`, and because of that we had to
suppress a warning from mypy on line 10, using a `# type: ignore`. If you remove
that comment, mypy will say "we expected to return a `T`, but this `wrapper`
function can be anything". However we know that we're not changing the signature
so it is safe to ignore this warning. To do that, we add a `# type: ignore`.

But with that, our decorator is fully typed. It can take in functions of any
kind, and wrap them without erasing any type information.
