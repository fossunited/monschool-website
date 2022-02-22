---
title: The "Any" type
include_in_preview: false
---

We've come really far in our typing journey, learning how to annotate, test and
fix the types by using our friendly tool `mypy`. And truth be told, I really
enjoy using mypy to figure out type inconsistencies in code, and making it more
robust.

But there's a small problem with this: sometimes you don't want to define a
strict type for a part of your code. Some other times, you actually _can't_
define an exact type. This all stems from the fact that Python is an extremely
dynamic language. You can read arbitrary data from files and convert it into
objects at runtime. You can even do crazy things like defining new classes while
the code is running!

And because of how dynamic Python is, it is impossible to statically type some
kinds of Python code. It's what makes Python a powerful language in the first
place.

A common example of such a pattern is _duck typing_:

```{.python .example}
def do_quack(duck):
    if hasattr(duck, "quack"):
        quack_function = duck.quack
        quack_function()
    else:
        print("Expected an object with a 'quack' method.")

class Goose:
    def quack(self):
        print("Goose goes 'quack'.")

goose = Goose()
do_quack(goose)
```

The fact that we can look up if the passed object has a `quack` method on it,
allows us to pass any kind of object that "can quack", be it a `Duck`, or a
`Goose`, or something else entirely.

For this code, even if we were able to add types to the code, mypy simply can't
figure out the type of `quack_function`, because `duck.quack` can be anything
depending on the object passed.

For this reason, usually what you do is tell mypy to just ignore checking this
object when type checking. You do this by using the `Any` type from the `typing`
module:

```{.python .example}
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

Doing this will essentially let you do anything with the `duck` object, even
things that will crash at runtime. `Any` tells mypy to leave testing this code
for the developers. Whenever possible, you should try to avoid using `Any`.

We'll be looking into duck typing at a much deeper level, and mitigating the use
of `Any` in such cases in the next chapter.

Another common example is when you don't know the exact type of something. Let's
say you have to build a library around an API, that returns some data for your
users. The API is currently in development, and the data returned by the API can
change at any time:

```{.python .example}
data = {
  'name': 'Mr. User',
  'age': 33,
  'identity_proofs': ['Passport', 'Birth Certificate'],
  'is_employed': True,
}
```

The data object currently contains things like strings, ints and lists, but it
can change in the future at any time, and you want to avoid spending time
defining exact types for this data, until it is finalized. You can also use
`Any` for this case:

```{.python .example}
from typing import Any

def pretty_print_data(user: Any) -> None:
    print(f"User {user['name']} is {user['age']} years old.")
    print(f"They have provided {user['identity_proofs']} as their IDs.")

data = {
  'name': 'Mr. User',
  'age': 33,
  'identity_proofs': ['Passport', 'Birth Certificate'],
  'is_employed': True,
}
pretty_print_data(data)
```

This way, you can use mypy to validate the rest of your code, and come back to
this part of the code later.
