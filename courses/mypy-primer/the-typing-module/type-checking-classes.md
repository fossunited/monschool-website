---
title: Type checking your classes
include_in_preview: false
---

The next step up from functions, unsurprisingly, is classes. Fortunately type
checking classes is very straightforward: Just add hints to the methods for the
most part and you'll be good.

Here's an example class, that just implements a stack of numbers:

```{.python .example}
class Stack:
    def __init__(self):
        self._values = []

    def __repr__(self):
        return f'Stack{self._values!r}'

    def push(self, value):
        self._values.append(value)

    def pop(self):
        if len(self._values) == 0:
            raise RuntimeError('Underflow!')

        return self._values.pop()

stack = Stack()
print(stack)

stack.push(2)
stack.push(10)
print(stack)

popped_value = stack.pop()
print("Popped value:", popped_value)
print(stack)
```

Running the code, you can see that the stack gets values put into it and popped
out of it. If you pop on an empty stack, you'll get an Underflow error.

Let's see what mypy says about it, and add type annotations as necessary:

First off, mypy complains about a lot of untyped definitions. The functions
need annotation. And before you do that, think about this:

`def __init__(self):`

What should the type of `self` be?

Since it's an object of the `Stack` type, it would make sense to do:

`def __init__(self: Stack) -> None:`

Right? Well, kindof. The problem then arises when you try to subclass `Stack`
into some other type:

```python
class SubStack(Stack):
    ...
```

Since the `__init__` method is inherited, and `self` is supposed to be of type
`Stack`, mypy would thinkg `SubStack` creates objects of `Stack` type. Clearly
that won't work.

To avoid problems with inheritence, mypy decided that `self` does not need to be
given a type annotation. You must leave the first argument of a method untyped.

So our annotations look something like this:

`def push(self, value: int) -> None:`

Here's what the class looks like after annotating the function signatures:

```{.python .example}
class Stack:
    def __init__(self) -> None:
        self._values = []

    def __repr__(self) -> str:
        return f'Stack{self._values!r}'

    def push(self, value: int) -> None:
        self._values.append(value)

    def pop(self) -> int:
        if len(self._values) == 0:
            raise RuntimeError('Underflow!')

        return self._values.pop()
```

Although looking at mypy's output, it still isn't sure about some things. Can
you guess why?

It's because of the empty list instantiation inside `__init__`. Mypy needs to
know what kinds of items you want to be in the list. The second error stems from
the same fact: Since mypy doesn't know what the type of `self._values` is, it
can't determine what `self._values.pop()` should return.

To fix that, replace the definition with this:

`self._values: list[int] = []`

And now we have fully annotated a class. Wasn't it really easy? That's pretty
much how it goes with mypy, 90% of your work is adding types to function
definitions, and mypy takes care of validating the rest.

### Aside: exceptions

Notice the definition of `pop` in the `Stack` class:

```python
    def pop(self) -> int:
        if len(self._values) == 0:
            raise RuntimeError('Underflow!')

        return self._values.pop()
```

In case of an underflow, the function raises an exception. The function doesn't
return an `int` in that case. So you might think that the type signature isn't
fully correct: Sometimes we return `int`, but sometimes we don't. And yet mypy
is fully convinced that the signature is perfectly good. Why is that?

Take this code for example:

```{.python .example}
def only_evens(number: int) -> int:
    if number % 2 != 0:
        raise ValueError("Not even!")

    return number

number = 2
even_number = only_evens(number)
print(even_number, "is an even number.")
```

Mypy says the function is okay. The code also works, but if you change `number`
to be `3`, we can see that the code crashes. What's going on?

Turns out, mypy is right (and almost always, it will be). When `only_evens`
raises an error, the normal execution of the code stops, and the error is
propagated up to the user. Which means that if `number` is odd, because of the
raised error, `even_number` variable will never be created.

The important thing to note about this code snippet is this: If `even_number` is
ever created, it is guaranteed to be an `int`. So the return type of the
function is accurate. Whenever the function returns a value, it is 100%
guaranteed to be `int`. The types are correct.
