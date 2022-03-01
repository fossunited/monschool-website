---
title: The Type type
include_in_preview: false
---

`Type` is a type used to type classes. It derives from python's way of figuring
out the type of an object at runtime:

```{.python .example}
a, b = 1, 2
s = 'hello'

print(type(a))             # <class 'int'>
print(type(b))             # <class 'int'>
print(type(a) == int)      # True
print(type(a) == type(b))  # True
print(type(a) == type(s))  # False
```

Since `type(x)` returns the class of `x`, the type of a class `C` is `Type[C]`.

```{.python .example}
from typing import Any, Type, TypeVar

class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def __repr__(self) -> str:
        return f'C(x={self.x})'


T = TypeVar('T')

def make_object(cls: Type[T], *args: Any) -> T:
    print('making object of', cls)
    obj = cls(*args)
    return obj


c = make_object(MyClass, 42)

print(c)
print(c.x)
```

We have now made a function that can take in classes as arguments. Doing
`reveal_type(c)` correctly tells us that it's an object of `MyClass`.
