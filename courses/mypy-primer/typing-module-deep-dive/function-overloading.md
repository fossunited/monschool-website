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

We're essentially telling mypy that we know `double(16)` will return an `int`,
not `int | str`. Overloads aren't validated by mypy yet, we have to ensure
ourself that we specify the right overloads.

Also, the `@overload` decorator doesn't do anything at runtime. It's yet another
way to provide extra type information to mypy. It's important that you keep the
actual definition of `def double` *below* the overloads, otherwise the overload
definition will overwrite your actual function.

---

Let's see a few more examples of overloads and why we'd use them. Here's an
`average` function that has two separate behaviours: round the result, or don't
round it:

```{.python .example}
def average(x, y, rounding):
    average = (x + y) / 2
    if rounding:
        return round(average)
    else:
        return average

print(average(2, 5, rounding=False))
print(average(2, 5, rounding=True))
```

When `rounding` is `False`, we return a `float`, but when it's `True` we return
an `int`. So we can define these overloads:

```{.python .example}
from typing import overload

@overload
def average(x: int, y: int, rounding: True) -> int: ...

@overload
def average(x: int, y: int, rounding: False) -> float: ...
```

Though if you try to do that, mypy will complain, and suggest using `Literal`.
What `Literal` does is define a type that can accept a specific set of constants
as the value. For example, a variable of type `Literal[True]` will only ever
accept `True` as a value, while `Literal['get', 'post']` will accept either the
string `'get'` or `'post'`. So let's use that to define the overloads:

```{.python .example}
from typing import Literal, overload

@overload
def average(x: int, y: int, rounding: Literal[True]) -> int: ...

@overload
def average(x: int, y: int, rounding: Literal[False]) -> float: ...


def average(x: int, y: int, rounding: bool) -> int | float:
    average = (x + y) / 2
    if rounding:
        return round(average)
    else:
        return average

print(average(2, 5, rounding=False))
print(average(2, 5, rounding=True))
```

If you do `reveal_type(average(2, 5, rounding=False))` you'll see we get `float`
and `reveal_type(average(2, 5, rounding=True))` gets `int`.

One more example: a function that can take either one or two arguments:

```{.python .example}
def add(x, y=None):
    if y is None:
        return x + 1
    
    return x + y

print(add(1, 1))
print(add(5))
```

`add(5)` just increments `5` to `6`. Typing it is also simple with `@overload`:

```{.python .example}
@overload
def add(x: int) -> int: ...

@overload
def add(x: int, y: int) -> int: ...

def add(x: int, y: int | None = None) -> int:
    if y is None:
        return x + 1
    
    return x + y
```

Another interesting side effect of this overload is the fact that now we only
have two possible signatures of `add`: one `int` or two `int`s.

Without an overload, doing `add(5, None)` would be valid code, and would be the
same as `add(5)`, but we don't want people to be able to do that. Using
`@overload` lets us disallow that as well.
