---
title: Union and Optional types
include_in_preview: false
---

We've seen that mypy says that this is an error:

```{.python .example}
var = 123
var = 'abc'
```

But what if you actually wanted to do this?

It might seem like you'd never want to do this, but consider this example:

```{.python .example}
chosen_number = "not found"

for number in [1, 5, 7, 4]:
    if number % 2 == 0:
        chosen_number = number

print("Chosen number:", chosen_number)
```

`chosen_number` is going to end up as an integer in some cases, but if the list
doesn't have any even integers in it, it will stay as its default value of
`"not found"`. And mypy is confused by this.

In this case, we intentionally want `chosen_number` to be able to hold both the
string default, and the possible integer values. And to tell mypy that this is
our intention, we need to expand its knowledge on what the type of the variable
should be.

Due to the definition, it's assuming that `chosen_number` should be of type
`str`:

```{.python .example}
chosen_number = "not found"
reveal_type(chosen_number)
```

But we don't want that, we want the variable to be able to accept "either `str`
or `int` values". And for that, you use the `Union` type from the `typing`
module:

```{.python .example}
from typing import Union

chosen_number: Union[str, int] = "not found"

for number in [1, 5, 7, 4]:
    if number % 2 == 0:
        chosen_number = number

print("Chosen number:", chosen_number)
```

Now that mypy correctly knows that we want it to have either kind of values, it
tells us that the rest of the code is good.

Note that `Union` can take any number of types, not just two. For example, a set
that can contain strings, integers and floats would be typed as
`set[Union[str, int, float]]`.

## Some examples and caveats

Remember when we talked about a better way to make a collection type with
multiple data types in it? The example we used was:

```{.python .example}
items = [1, 2, 3]
items.append(4)
items.append('world')
```

The old solution that we used was to use `list[object]`, but that lends us into
this problem:

```{.python .example}
items = [1, 2, 3]
items.append(4)
items.append(False)
items.append({'this is': 'a dictionary'})
```

Yeah, with `list[object]` you can suddenly append any object into the list. To
limit it to just ints and strings, just use a union:

```{.python .example}
from typing import Union

items: list[Union[int, str]] = [1, 2, 3]
items.append(4)
items.append('world')

# Now these don't work anymore!
items.append(False)
items.append({'this is': 'a dictionary'})
```

Cool right?

However, consider this:

```{.python .example}
from typing import Union

items: list[Union[int, str]] = [1, 2, 3]
items.append(4)

total = 0
for item in items:
    total += item

print(total)
```

Although this code works, now mypy says we're doing something wrong. The error
says:

```console
Unsupported operand types for `+`: "int" and "str"
```

What this means is that in our addition operation, the left hand value is an
`int`, and the right hand value is a `str`:

```python
    ...
    total += item
```

Mypy is worried, that since we said `items` _can_ have strings in it, it's
possible that `item` is of type `str`. So it won't let you do this as it is code
that can possibly crash. To solve this, we need to do something called "type
narrowing".

## Type narrowing

To be fair, there is a bug in our code. If we make the list this:

```{.python .example}
from typing import Union

items: list[Union[int, str]] = [1, 2, 3, "A string"]
items.append(4)

total = 0
for item in items:
    total += item

print(total)
```

Python suddenly crashes with the same error that mypy was previously warning us
about. And since we did tell mypy that we want to put strings in the list, it's
completely understandable for mypy to give us this warning. Mypy always wants to
make sure that our code doesn't crash at runtime.

So, how do we fix the code? Well, we could just check if each item is an `int`
before adding it to the total:

```{.python .example}
from typing import Union

items: list[Union[int, str]] = [1, 2, 3, "A string"]
items.append(4)

total = 0
for item in items:
    if isinstance(item, int):
        total += item

print(total)
```

... and now mypy correctly shows no errors! Great. Mypy understands that inside
the `isinstance` block, `item` can _only_ be an integer. You can even confirm it
by doing `reveal_type`:

```{.python .example}
from typing import Union

items = [1, 2, 3, "A string"]
items.append(4)

total = 0
for item in items:
    reveal_type(item)
    if isinstance(item, int):
        reveal_type(item)
        total += item
```

Here's what we learned: You can use `isinstance` blocks that only run if the
data is of a certain type, to narrow down a union of types to the one that we
want. Here's another example:

```{.python .example}
from typing import Union

def buy(stuff: Union[str, list[str]]) -> None:
    if isinstance(stuff, list):
        # Buy every item in the list
        for item in stuff:
            print("Buying {item}")

    else:
        # Buy the one item
        print("Buying {stuff}")


buy("Jam")
buy(["Milk", "Eggs", "Spam"])
```

Because we checked for `list`s, Mypy understood that `list[str]` is the only
possible type for `stuff`. On the other hand, inside the `else` block, `stuff`
is seen as a string:

```{.python .example}
from typing import Union

def buy(stuff: Union[str, list[str]]) -> None:
    if isinstance(stuff, list):
        reveal_type(stuff)
        ...

    else:
        reveal_type(stuff)
```

## Optional

Take this function:

```{.python .example}
def pop_word(words):
    """Takes one word out of given words."""
    if len(words) == 0:
        print("Warning: empty list")
        return None

    word = words.pop()
    return word

word = pop_word(['foo', 'bar'])
```

What should the type definition of the above code be?

If you answered:

```python
def pop_word(words: list[str]) -> Union[str, None]:
    ...
```

Then you'd be correct! It's actually really common to see types that look like
`Union[A, B, None]`, that the `typing` module has a shortcut for it, called
`Optional`. Any instance of `Union[A, B, ..., None]` can be replaced with
`Optional[A, B, ...]`.

For example, `Union[int, None]` can be written as `Optional[int]`, and
`Union[str, bool, None]` as `Optional[str, bool]`.

## New syntax

Just like the use of `list` instead of `typing.List`, `Union` has also become
unnecessary starting from Python 3.10. If you're going to run your code on 3.10
or higher, you can use this syntax instead:

```{.python .example}
items: list[int | str] = [1, 2, 3]
```

The `|` operator can be used with as many types as you want to make the same
unions as you'd make with `Union[...]`. `int | str` means the same thing: Either
`int` or `str`.

Similarly, `Optional[bool]` can be written as `bool | None`, here's an example:

```{.python .example}
user = {
    'name': 'Bryan',
    'likes': ['parkour', 'dogs']
}

def likes_flowers() -> bool | None:
    like_data = user.get('likes')
    if like_data is None:
        # We don't have likes data
        return None

    if 'flowers' in like_data:
        return True
    else:
        return False
```

Again, I'll be using the new `|` syntax for the rest of the course, for
simplicity's sake. Feel free to use either yourself.
