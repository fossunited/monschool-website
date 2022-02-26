---
title: Function overloading with @overload
include_in_preview: false
---

Another fairly common pattern in Python is polymorphic functions, i.e. functions
that can take various types of arguments and behave differently. Take this silly
function for example:

```{.python .example}
def double(item):
    if isinstance(item, str):
        return f'2 {item}s'
    
    return item + item

print(double('cookie'))
print(double(16) + 10)
```

We've already seen some code like this in the "type narrowing" section before.
Let's try to add types to it:

```{.python .example}
def double(item: str | int) -> str | int:
    if isinstance(item, str):
        return f'2 {item}s'
    
    return item + item

print(double('cookie'))
print(double(16) + 10)
```

Notice the problem? Mypy says that since the function returns `str | int`, you
can't add an `int` to it. Because it could be a `str`. But we didn't mean that
what we actually meant was: "If you get a `str` you return a `str`, and if you
get an `int` you return an `int`. Overloads were designed to be able to express
this notion. They're used like this:

```{.python .example}
from typing import overload

@overload
def double(item: str) -> str: ...

@overload
def double(item: int) -> int: ...

def double(item: str | int) -> str | int:
    if isinstance(item, str):
        return f'2 {item}s'
    
    return item + item

print(double('cookie'))
print(double(16) + 10)
```
