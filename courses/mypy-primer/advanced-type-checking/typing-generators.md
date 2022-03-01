---
title: Type checking generators
include_in_preview: false
---

Generators are really useful. They're lazy iterators that are really easy to
create and compose. It leads to writing very readable and efficient code when it
comes to manipulating lists of data.

Here's an example of how it can be useful:

```{.python .example}
def odd_squares() -> list[int]:
    result = []
    for num in range(2_000_000):
        square = num ** 2

        if square % 2 != 0:  # check if odd
            result.append(square)

    return result

print("Getting squares...")
for number in odd_squares():
    if number > 100:
        break

    print(number)
```

Note that it takes quite a long time to calculate all the squares at once. The
code calculates a million squares, returns them, and then we use the first five
and throw away all the other work. What a waste.

Generators allow us to avoid this, by only calculating each next value when we
ask for it. Converting the code to use generators is fairly simple:

```{.python .example}
def odd_squares():
    for num in range(2_000_000):
        square = num ** 2

        if square % 2 != 0:  # check if odd
            yield square

print("Getting squares...")
for number in odd_squares():
    if number > 100:
        break

    print(number)
```

We just got rid of the `results` array, since we aren't storing the numbers
beforehand. As we calculate each odd square, we `yield` the value out to the
`for` loop. This way, as soon as the `for` loop is broken out, we stop producing
the values. No wasted calculations.

Now let's get to adding types to this thing! Generator functions that have a
`yield` statement in them always return a generator object, and we will simply
annotate the return type of the function as such. There's actually quite a few
ways to do that, the simplest being to just make it as an `Iterator`:

```{.python .example}
from typing import Iterator

def odd_squares() -> Iterator[int]:
    for num in range(2_000_000):
        square = num ** 2

        if square % 2 != 0:
            yield square

print("Getting squares...")
for number in odd_squares():
    if number > 100:
        break

    print(number)
```

Generators are also Iterators. It's obvious by the fact that they're being used
in a `for` loop, which only accepts iterators. Since generators are valid
iterators, duck typing indicates that we can just use `Iterator` as their type.
How simple!

### Typing Complex Generators

Generators have a bit more functionality than that. Not only can they `yield`
values out of them, they can also accept values in, when they run again to yield
the next value. This makes them a great tool to write "coroutines": programs
that communicate data back and forth.

Here's an example, where we send data to a generator that doubles our number,
and we send it back the number incremented by one:

```{.python .example}
def doubler():
    num = yield 0  # To get the first value

    while True:
        double = num * 2
        num = yield double

double = doubler()

# This is required, to pause it at `yield 0`.
# That way we can start passing values to `num`.
double.send(None)

num = 0
while num < 100:
    # Step 1: add 1
    num += 1
    print(f"Plus one: {num}")

    # Step 2: double it
    num = double.send(num)
    print(f"Doubled:  {num}")

print("Done.")
```

You can try to type annotate this method like before:

```{.python .example}
from typing import Iterator

def doubler() -> Iterator[int]:
    num = yield 0  # To get the first value

    while True:
        double = num * 2
        num = yield double

double = doubler()
double.send(None)
```

But that will give you two errors. This is because of the difference between an
iterator and a generator: While iterators implement `iter` and `next` to support
for-loops, they don't require a `.send` method like generators. And since you
marked `doubler()` to return an `Iterator`, mypy says it's possible that it
doesn't have a `.send()` method.

We also get another error saying `num` got `None` when it expected `int`. Since
an `Iterator` doesn't have a `.send` method, in iterators the `yield` always
returns `None`, so mypy doesn't know what type the sent data should be.

We solve both these issues by using `typing.Generator` instead. It uses this
syntax:

`Generator[YieldType, SendType, ReturnType]`.

So we can do this:

```{.python .example}
from typing import Generator

def doubler() -> Generator[int, int, None]:
    num = yield 0  # To get the first value

    while True:
        double = num * 2
        num = yield double

double = doubler()
next(double)

num = 0
while num < 100:
    num += 1
    print(f"Plus one: {num}")

    num = double.send(num)
    print(f"Doubled:  {num}")

print("Done.")
```

> We also replaced `double.send(None)` with the equivalent `next(double)`.

The third argument, `ReturnType`, isn't used in almost any use case, and is
usually left as `None`, but if you end up returning something from a generator
it's pretty simple to use its type as the 3rd argument.

Also, in our case, both the sent data and yielded data are `int`s, but you can
similarly make a generator that has different `send` an `yield` types, like so:

```{.python .example}
from typing import Generator

def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

nums = [1.2, 4.7, 6.0]

rounder = echo_round()
next(rounder)

for num in nums:
    print(num, '->', rounder.send(num))
```
