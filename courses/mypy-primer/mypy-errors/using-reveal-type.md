---
title: Using reveal_type() to debug types
include_in_preview: false
---

The last fundamental feature I want to introduce about mypy is the existence of
the `reveal_type` function.

This function doesn't actually exist in Python, in the `typing` module, or
anywhere else. But mypy understands it. `reveal_type` is used to ask mypy
about what it thinks the type of a variable is.

Here's a quick demo:

```{.python .example .mypy-strict}
string = "This is a string"
length = len(string)
reveal_type(length)
```

So we're able to know that mypy thinks that `length` is an integer. But if you
try to run the code, it will immediately crash, saying `reveal_type` is not
defined.

And this is a feature -- this ensures you don't accidentally leave a
`reveal_type` statement in your code after you're done debugging. Also When you
use `reveal_type`, mypy exits with an error code, saying that the code isn't
currently in working shape.

But the important part is, now you can easily know what mypy is thinking about
your code, and you can debug your types.

## An old friend

Let's use `reveal_type` to debug an older code example that we saw and fixed:

```{.python .example .mypy-strict}
import json
from itertools import cycle

items_json = """
{
    "items": [
        "item 1", "item 2", "item 3", "item 4", "item 5",
        "item 6", "item 7", "item 8", "item 9", "item 10"
    ]
}
"""

def get_worker_count(): return 4

def run_processes() -> None:
    worker_count = get_worker_count()
    print("Running with " + worker_count + " workers")

    workers = range(worker_count)

    items = json.loads(items_json)
    reveal_type(items)
    for item, worker in zip(items, cycle(workers)):
        print(f"Processing {item} with worker {worker}")


if __name__ == "__main__":
    run_processes()
```

> Remember to comment out the `reveal_type` lines when trying to run the code!

Using reveal_type, we see a new result: it says the type of `items` is `Any`.

We'll talk about `Any` type and its uses in detail in the next chapter, but you
can understand it basically saying "`items` can be anything". Mypy has no idea
what it can be.

With the fixed code, mypy understands the types correctly:

```{.python .example .mypy-strict}
import json
from itertools import cycle
from time import sleep

items_json = """
{
    "items": [
        "item 1", "item 2", "item 3", "item 4", "item 5",
        "item 6", "item 7", "item 8", "item 9", "item 10"
    ]
}
"""

def get_worker_count() -> int: return 4

def run_processes() -> None:
    worker_count = get_worker_count()
    print("Running with " + str(worker_count) + " workers")

    workers = range(worker_count)

    data = json.loads(items_json)
    items = data['items']
    assert isinstance(items, list)
    reveal_type(items)

    for item, worker in zip(items, cycle(workers)):
        reveal_type(item)
        reveal_type(worker)
        print(f"Running {item} with worker {worker}")


if __name__ == "__main__":
    run_processes()
```

Now mypy is confident that `items` is a list. But what does it contain? No idea.
Could be anything. Similarly, checking the types of `item` and `worker`, we get
`Any` and `int` respectively. Worker is definitely an integer, but item can still
be anything. Which is alright: `print` can print anything out so mypy is okay
with the code.

Hopefully that explains a lot more about mypy's workings. Feel free to make
changes to the code, and use `reveal_type` to figure out what mypy thinks.
