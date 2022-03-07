---
title: Static duck typing
include_in_preview: false
---

Welcome to chapter 4, we're already half-way through the course! It is now time
to really dive into the deep end with typing, and start learning how to add
type hints to the more uncommon Python syntax and code styles.

And we're starting with probably the most common Python code pattern, called
"duck typing".

Duck typing is essentially a way that Python uses to make its functions really
flexible. Instead of expecting an object of a specific class, these functions
will be fine with an object of *any* type, as long as it satisfies some
conditions. These conditions are usually specific properties or methods being
present on the object. As long as they're available, the code works.

We've already seen an example of this in the course, although a much more
simplified one:

```{.python .example .mypy-strict}
from typing import Any

def do_quack(duck: Any) -> None:
    if hasattr(duck, "quack"):
        quack_function = duck.quack
        quack_function()
    else:
        print("Expected an object with a 'quack' method.")

class Goose:
    def quack(self) -> None:
        print("Goose goes 'quack'.")

goose = Goose()
do_quack(goose)
```

`do_quack` only cares about the `quack` method being present, and nothing else.
If it is there, it calls the method. But it's not that great -- You can still
pass anything to `do_quack`, and if it doesn't, the function simply returns
without doing anything. That's not very good.

Let's go the other way around, by asking for a concrete type:

```{.python .example .mypy-strict}
class Duck:
    def quack(self) -> None:
        print("Duck goes 'quack'.")

def do_quack(duck: Duck) -> None:
    duck.quack()

class Goose:
    def quack(self) -> None:
        print("Goose goes 'quack'.")

goose = Goose()
do_quack(goose)
```

This code 'works', but mypy complains that it expected an object of type `Duck`.
You could just extend `Goose` from `Duck`:

```{.python .example .mypy-strict}
class Duck:
    def quack(self) -> None:
        print("Duck goes 'quack'.")

def do_quack(duck: Duck) -> None:
    duck.quack()

class Goose(Duck):
    def quack(self) -> None:
        print("Goose goes 'quack'.")

goose = Goose()
do_quack(goose)
```

Now mypy is happy, and the code works! And traditionally, this has been the
solutions in statically typed languages: just use inheritance. But this comes
with the big problem that your code is now coupled to `Duck`: If `Duck` adds new
behaviour, you add new behaviour too. In general, it's not as flexible.

What we *really* need, is a way to make `Duck` a type that can accept any type
that implements `quack`. This concept is called a `Protocol` in Python:

```{.python .example .mypy-strict}
from typing import Protocol

class Duck(Protocol):
    def quack(self) -> None:
        pass

def do_quack(duck: Duck) -> None:
    duck.quack()

class Goose:
    def quack(self) -> None:
        print("Goose goes 'quack'.")

goose = Goose()
do_quack(goose)
```

It works! Now mypy knows what we expect from a `Duck`. So as long as `Goose`
satisfies the `Duck` protocol, mypy is fine with it. If you remove the `quack`
method from `Goose`, or if you change its return type or signature, the type
checking will start to fail. It's as simple as that.

Note that we completely got rid of the `hasattr(duck, "quack")` part of the code
from the first example. That's because mypy will be checking if the code is fine
or not anyway, we don't need to confirm it anymore at runtime. As long as we use
mypy, we can rest assured.

> Also note that we didn't provide any method body to `Duck.quack()`. That's
> because we're only interested in defining the method signature in a protocol
> class, not the actual contents inside it. So, mypy simply ignores the content.
> Traditionally, you're supposed to use `...` for the body of a protocol method.
> We'll do that in the next example.

There's a lot more that can be done using protocols. A nice example would be the
"callable" protocol:

```{.python .example .mypy-strict}
def func() -> int:
    return 42

class FuncGenerator:
    def __call__(self) -> int:
        return 42

func2 = FuncGenerator()


print(func())
print(func2())
```

In Python, you can create your own objects that are "callable", i.e. you can run
them like a function, if you define a `__call__` method on that object's class.
This function is run when you do `obj()`. This is an excellent place for using a
protocol:

```{.python .example .mypy-strict}
from typing import Protocol

class Callable(Protocol):
    def __call__(self) -> None: ...


def call_twice(function: Callable) -> None:
    """Calls the given function twice."""
    function()
    function()


def fortytwo() -> None:
    print(42)

class Counter:
    def __init__(self) -> None:
        self.count = 1

    def __call__(self) -> None:
        print("Call count:", self.count)
        self.count += 1

counter = Counter()

call_twice(fortytwo)
call_twice(counter)
```

We were able to create our own "callable" counter object, and pass it to
`call_twice`, all while mypy being able to ensure our code will run fine.

Another example would be the "iterable" protocol. It refers to any object that
can be iterated over using a `for` loop, like this for example:

```{.python .example .mypy-strict}
def count_unique(items: list[str]) -> int:
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

While the code works, we get an error telling us that we passed a
`dict_values[int, str]`, where `list` was expected. Basically it's telling us
that `greetings.values()` does not return a list.

But does that really matter to us? I don't think so. We do know that
`greetings.values()` returns us something that *resembles* a list, and we can
definitely iterate over it:

```{.python .example .mypy-strict}
greetings = {1: 'hello', 2: 'hi', 3: 'hello'}
for greeting in greetings.values():
    print(greeting)
```

And all we care about is the item being *iterable* and having strings inside it,
what we really want is a protocol:

```{.python .example .mypy-strict}
from typing import Protocol

class StringIterator(Protocol):
    def __next__(self) -> str: ...

class StringIterable(Protocol):
    def __iter__(self) -> StringIterator: ...

def count_unique(items: StringIterable) -> int:
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

It might be a bit confusing seeing two protocols here, but that's just how
Python does iteration. When you do a `for` loop on any object in Python, it
does two things:

- It calls `iter(obj)` on that object, which returns an "iterator" object.
- Python will then repeatedly call `next(iterator)` until it no longer contains
  a value.

To support this, we need to define both an "iterable" type and an "iterator"
type. The `StringIterable` expects to find a `__iter__` method on the object,
and `StringIterator` expects to get a string back on every iteration.

A list of strings and `greetings.values()` both satisfy this definition, as both
can be passed to a `for` loop, and both return strings. So mypy is happy with
the protocol. In fact, you can now pass a tuple of strings, a set of strings,
and a lot of other kinds of types into the function, and it will all work.

I hope that you're thinking "this seems like it'd be a very common type to use",
and you're right. The typing module already has an `Iterator` and an `Iterable`
type defined in it. Though they are slightly different. We will take a look at
them in the next section.
