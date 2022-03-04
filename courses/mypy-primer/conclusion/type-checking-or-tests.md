---
title: Type checking, or writing tests? Why not both!
include_in_preview: false
---

Ever since static and dynamic typed languages have existed, there has existed an
argument between them, one that argues what's better: type checking, or writing
tests.

The argument essentially boils down to these two sides: The dynamic side would
say something like, "I've been writing python for so long without types, why
should I care now?", or, "I don't need types in my code because I write tests".
Conversely, people can think they don't need tests (at least not as much as
dynamic languages) because their type checker catches their bugs for them.

The truth is that both of these arguments are extreme, and this, both are wrong.
The correct answer lies somewhere between them. I think both static types and
tests are equally necessary in a large codebase, because *they both serve a
different purpose*.

### Why types

Type checking eliminate a whole class of bugs from your codebase: type errors.

Writing good tests is hard, especially in a dynamically typed language. It's
very easy to write tests that forget to check all the possible invalid types
that you could pass to the function. For example:

```{.python .example}
def process(items):
    for item in items:
        print("Processing", item.value.id)
```

It is very easy to write 5 different passing tests for this code, but forget to
write a test where `value` is `None`. If it is `None`, you'll get an attribute
error raised at runtime.

If the schema of each `item` object was well defined beforehand, the problem
would've easily been caught beforehand:

```{.python .example}
from dataclasses import dataclass
from typing import Iterable

@dataclass
class ItemDetails:
    id: int
    name: str

@dataclass
class Item:
    value: ItemDetails | None
    weight: int

def process(items: Iterable[Item]) -> None:
    for item in items:
        print("Processing", item.value.id)
```

Now mypy will catch that problem for you. Same goes for if someone tries to pass
something completely wrong to `process`, like a dictionary. Mypy has taken the
burden of handling completely invalid usage of your code away from you, so that
you can focus on the fine details.

### Why tests

Tests are important, because they are necessary for checking your logic.
Logical errors can't be possibly tested through type checking. For example,
here's a perfectly type checked code:

```{.python .example}
def sum(a: int, b: int) -> int:
    return (a + b) // 2
```

This is a really obvious example, but real world scenarios can be much more
complicated than this. You can't expect a code analysis tool to figure out
problems like deadlocks, missing `else`-clauses, incomplete or invalid logic,
etc. Thus, testing your code and all its possible outputs is an essential part
of developing a big project.

*Both type checkers and tests work in unison*: Type checking takes away the task
of identifying and fixing inputs to your code that are obviously invalid, such
as passing a `str` instead of `int`. Tests on the other hand, prevent more fine
grained bugs, that can come from logical errors and the like.

So my advice would be to use both tests and types -- so that you can be
completely confident in your code's correctness.
