---
title: Custom Generic types
include_in_preview: false
---

We've seen many generic types before, `list` and `dict` to name a few. They're
super useful when you want to create a container data type, or any type that can
be defined as a composition of other types.

Remember the `Stack` class we defined a while ago? That one only worked with
integers, but it didn't really have to. If you try to run it with strings
instead, it will still work just fine. This is a good indication that `Stack`
should've been a generic type. So let's do that:

```{.python .example}
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._values: list[T] = []

    def __repr__(self) -> str:
        return f'Stack{self._values!r}'

    def push(self, value: T) -> None:
        self._values.append(value)

    def pop(self) -> T:
        if len(self._values) == 0:
            raise RuntimeError('Underflow!')

        return self._values.pop()

stack: Stack[int] = Stack()
stack.push(1)

stack2: Stack[str] = Stack()
stack2.push('a')
```

There's 3 steps in making a class generic:

- Create a `TypeVar`. The syntax for making it is a bit odd, where you have to
  pass it its own name in a string, like so: `T = TypeVar('T')`.
- Make your class extend `Generic[T]`. This doesn't do anything at runtime, but
  it tells mypy that we want the class to take in a type in its definition.
- Anywhere that our type would depend on the chosen type, we use `T` instead of
  the actual type. In our case, `self._values` becomes of type `list[T]` instead
  of `list[int]`, and all `int`s get replaced with `T` in the methods.

Now our `Stack` is generic! If we define it to be of type `Stack[str]`, it will
accept strings.

Note that we don't have to use just one type variable, we can use as many as we
want! We've already seen it with dictionaries for example: `dict[str, int]`.
Let's define a `Map` type that just wraps over a dictionary:

```{.python .example}
from typing import Generic, TypeVar

K = TypeVar('K')
V = TypeVar('V')

class Map(Generic[K, V]):
    def __init__(self) -> None:
        self._dict: dict[K, V] = {}

    def add_item(self, key: K, value: V) -> None:
        self._dict[key] = value

    def get(self, key: K) -> V | None:
        return self._dict.get(key)

m: Map[str, int] = Map()
m.add_item('some_key', 42)

print(m.get('some_key'))
print(m.get('other_key'))
```

Another really good candidate for generics would be the "iterable" that we made.
Our `StringIterable` and `StringIterator` protocols are pretty nice! But we can
take them a step further: by making them generic. Right now we have hard-coded
that we want `__next__` to return a `str`, but let's replace that with a type
variable so that we can extend it to any type we want:

```{.python .example}
from typing import Protocol, Generic, TypeVar

T = TypeVar('T', invariant=True)

class Iterator(Protocol, Generic[T]):
    def __next__(self) -> str: ...

class Iterable(Protocol, Generic[T]):
    def __iter__(self) -> Iterator[T]: ...

def count_unique(items: Iterable[str]) -> int:
    """Returns the number of unique items present"""
    unique_count = 0
    seen: set[str] = set()
    for item in items:
        if item not in seen:
            # We've seen a new unique item!
            unique_count += 1
            seen.add(item)

    return unique_count

count = count_unique(['10', '20', '20', '10'])
print(count)

greetings = {1: 'hello', 2: 'hi', 3: 'hello'}
unique_greetings = count_unique(greetings.values())
print(unique_greetings)
```

We just defined a generic protocol class! `Iterable` can now be an iterable of
any type `T`, and it returns an iterator of the same type. The only other
requirement was to tell `T` to be "invariant". For now, you can just think of it
as a requirement for protocols.

> Generic protocols are common enough that mypy accepts `Protocol[T]` as an
> alternative way to write `Protocol, Generic[T]`. So you can write
> `class Iterator(Protocol, Generic[T])` with `class Iterator(Protocol[T])` and
> the code will still work.

A really useful generic type would be a "generic callable" type. Where you could
define the types a callable would take in as arguments, and the return type.
Thankfully `typing.Callable` gives you exactly that:

```{.python .example}
from typing import Callable

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def call_function(func: Callable[[int, int], int]) -> None:
    print(func(3, 2))

call_function(add)
call_function(subtract)
```

`Callable` takes two arguments, a list of types (representing the arguments),
and the return type. Using it you can define any function's type to be able to
pass it to another function.

One last thing to learn would be defining generic functions. Take this function:

```{.python .example}
def make_pair(item: str) -> tuple[str, str]:
    return (item, item)

print(make_pair('abc'))
print(make_pair(42))
```

The code works, but the type hint prevents mypy from working. So let's just make
the function generic:

```{.python .example}
from typing import TypeVar

T = TypeVar('T')

def make_pair(item: T) -> tuple[T, T]:
    return (item, item)

print(make_pair('abc'))
print(make_pair(42))
```

Generics are useful in a lot of circumstances, and now you can use them in your
own code.
