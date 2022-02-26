---
title: Lists, Dictionaries, and other collections
include_in_preview: false
---

Okay, we've thoroughly covered the absolute basics, and now we're ready to dive
into the details, and learn more complex features of mypy and the `typing`
module in Python.

Let's start with one of the most necessary: annotating "collection types".

Collection types refer to things like lists, dictionaries and sets. The
difference between a basic type like `str` or `int`, and collections, is that
it's what's _inside_ the collection is what defines the type. For example:

```{.python .example}
var1 = [1, 2, 3]
var2 = ['a', 'b', 'c']
var3 = [True, False]
```

All the 3 variables are `list`s, but their types should be completely different.
You could argue as to why, but this should clarify it:

```{.python .example}
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

numbers.append(4)    # No error
letters.append('d')  # No error

letters.append(5)    # Mypy error
numbers.append('e')  # Mypy error
```

Mypy doesn't like the last two lines, because it saw that the original lists
had data of one specific type (`int` for the first list, `str` for the second),
so it figured that trying to add new data of a different type is probably
unintentional, or a bug.

Another example:

```{.python .example}
words = ['word1', 'word2']
words.append(['word3', 'word4'])
print(words)
```

If you try to run the code, you'll see that you accidentally got a list of words
inserted into the original list. In this case, the developer probably intended
to use `words.extend()` instead. Again, `mypy` flagged this as a bug.

Here's what it says:

```console
mycode.py:2: error: Argument 1 to "append" of "list" has incompatible type "List[str]"; expected "str"
```

`Argument 1 to "append" of "list"` refers to `['word3', 'word4']`. Mypy says it
expected a string, but it got a `List[str]` instead. What's `List[str]` you ask?
Well, it is the entire topic of this section.

## "Generics"

Collection types like `list` and `set` and a bunch of others are what's called a
"generic type". What it means is that the type takes another type to define its
instance. Here's what I mean:

```{.python .example}
var1 = [1, 2, 3]
reveal_type(var1)
var2 = ['a', 'b', 'c']
reveal_type(var2)
var3 = [True, False]
reveal_type(var3)
```

You can see that the data types of the variables is different. It's all lists (
it says `builtins.list` but that's just its way of saying `list`), but the part
inside the `[]` brackets is different: `int` for `var1`, `str` for `var2` and so
on. Essentially, `list` is a "generic type", and you can mold it to hold data of
any type that you want inside it.

## Generic type syntax

So far we've relied on mypy to tell us the type of lists. But you can't do that
for function definitions for example, you need to specify the kind of types a
function should expect. Take this function for example:

```{.python .example}
def buy(items):
    for item in items:
        print("Buying {item}")

buy(["Milk", "Eggs", "Spam"])
```

We want `buy` to take a list of strings. To do that we'll use the `[]` syntax
ourselves. But for it to work, we have to import the correct generic type from
the built-in `typing` module:

```{.python .example}
from typing import List

def buy(items: List[str]) -> None:
    for item in items:
        print("Buying {item}")

buy(["Milk", "Eggs", "Spam"])
```

The `typing` module has all the generic types you'll need:

```{.python .example}
from typing import List, Dict, Set

var1: List[int] = [1, 2, 3]
var2: Dict[str, bool] = {'married': True, 'single': False}
var3: Set[str] = {'a', 'b', 'c'}
```

Note that `Dict[str, bool]` is used to represent a dictionary with string keys
and boolean values.

Also, these types are composable, i.e. you can have a list of list of strings
for example:

```{.python .example}
def print_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        print(','.join(row))

# Sorry if you're hungry.
foods = [
  ["Eggs", "Ham"],
  ["Rice", "Bacon"],
  ["Bread", "Honey"],
]
print_matrix(foods)
```

Similarly, a dictionary with string keys and list of booleans as values would be
`Dict[str, List[bool]]`, for example.

### A small digression

A few of you might be thinking "Why do I have to import `List` when `list` is
already a Python data type?". And you're right, it's unnecessary to have to
import the "Generic types" when the builtin types already exist for you to use.

The good part is: You _can_ just use `list` and others, instead of importing
`List`:

```{.python .example}
var1: list[int] = [1, 2, 3]
var2: dict[str, bool] = {'married': True, 'single': False}
var3: set[str] = {'a', 'b', 'c'}
```

This just works! _But_, only if you're using Python 3.9 or above.

Doing `list[int]` before Python 3.9 would crash your code, it was only recently
added as a feature. Before that, the only way to do the annotation was to use
the `typing` module.

I wanted to ensure that you know about this fact, but for the rest of the course
we will be using the latest method of doing the annotations, i.e. `list[int]`
without the import.

---

One last thing: What if I actually _want_ to have multiple data types in my
collection type?

Well, if both the data types are already present in the definition, then you
don't need to do anything:

```{.python .example}
items = [1, 2, 3 'hello']
items.append(4)
items.append('world')
```

Mypy is fine with this. Why? It's because mypy looks at the contents of the list
and determines the lowest common ancestor of all types in the list. Since the
only common ancestor between the types `int` and `str` is `object` (all types
extend from `object`), the list ended up being of type `List[object]`.

But what if it's not? What if you want this to work?

```{.python .example}
items = [1, 2, 3]
items.append(4)
items.append('world')
```

One way to make it work is to explicitly tell mypy that we want a list of
`object`s:

```python
items: list[object] = [1, 2, 3]
items.append(4)
items.append('world')
```

There is a better way to do this though, as there are some problems with the
above method. We'll learn about that in the next section.
